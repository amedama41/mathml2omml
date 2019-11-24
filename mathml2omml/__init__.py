# pylint: disable=missing-docstring,fixme,too-many-lines
import itertools
import re
import xml.sax
import xml.sax.handler
import xml.sax.saxutils

from mathml2omml.op_dict import OP_DICT

INVISIBLE_CHARS = [
    '\u2061', # FUNCTION APPLICATION
    '\u2062', # INVISIBLE TIMES
    '\u2063', # INVISIBLE SEPARATOR
    '\u2064', # INVISIBLE PLUS
]
INVISIBLE_CHAR_PATTERN = '[%s]' % ''.join(INVISIBLE_CHARS)

def to_box(elem):
    if isinstance(elem, Element):
        return '<m:box>' + str(elem) + '</m:box>'
    return str(elem)

def to_element(elem):
    if not isinstance(elem, Element):
        return str(Element(elem))
    return str(elem)

def to_math_arg(elem):
    if isinstance(elem, Element):
        return ''.join(to_box(c) for c in elem.children)
    return str(elem)

class Element:
    def __init__(self, *children):
        self.children = list(children)

    def append(self, child):
        self.children.append(child)

    def __str__(self):
        return '<m:e>%s</m:e>' % ''.join(to_box(c) for c in self.children)

def op_attrs(operator, recommended_form='infix'):
    attrs = {
        'fence': False, 'separator': False,
        'lspace': 'thickmathspace', 'rspace': 'thickmathspace',
        'stretchy': False, 'symmetric': False,
        'maxsize': 'infinity', 'minsize': '100%',
        'largeop': False, 'movablelimits': False, 'accent': False,
    }
    content = operator.text().strip()
    for form in [recommended_form, 'infix', 'prefix', 'postfix']:
        dict_attrs = OP_DICT.get((content, form))
        if dict_attrs is not None:
            attrs.update(dict_attrs)
            attrs['form'] = form
            break
    else:
        attrs['form'] = 'infix'
    def try_to_bool(val):
        if val == 'false':
            return False
        if val == 'true':
            return True
        return val
    attrs.update((k, try_to_bool(v)) for k, v in operator.attrs.items())
    return attrs

class Pending:
    def __init__(self, base):
        self.base = base
        self.elements = []

    def append(self, elem):
        self.elements.append(elem)

    def fix(self):
        if self.elements:
            self.base.append(Element(*self.elements))
        return self.base

def _pop_opening_fence_elem(pending_stack, close_fence):
    while len(pending_stack) > 1:
        pending = pending_stack.pop()
        if not isinstance(pending.base, MFenced):
            pending_stack[-1].append(pending.fix())
            continue
        fence = pending.fix()
        fence.attrs['close'] = close_fence
        pending_stack[-1].append(fence)
        return
    fence = MFenced({'open': '', 'close': close_fence, 'separators': ''})
    fence.append(Element(*pending_stack[0]))
    pending_stack[0] = [fence]

def _append_elem(pending_stack, elem, recommended_form):
    if isinstance(elem, NaryableElement) and elem.is_nary():
        pending_stack.append(Pending(elem))
        return
    core_op = elem.embellished_op()
    if core_op is None or not isinstance(core_op, MO):
        pending_stack[-1].append(elem)
        return
    attrs = op_attrs(core_op, recommended_form)
    if not (attrs['fence'] and attrs['stretchy']):
        pending_stack[-1].append(elem)
        return
    form = attrs['form']
    if form == 'prefix':
        fence_attrs = {'open': core_op.text(), 'close': '', 'separators': ''}
        pending_stack.append(Pending(MFenced(fence_attrs)))
    elif form == 'postfix':
        _pop_opening_fence_elem(pending_stack, core_op.text())
    elif form == 'infix':
        for pending in reversed(pending_stack):
            if (isinstance(pending, Pending)
                    and isinstance(pending.base, MFenced)):
                _pop_opening_fence_elem(pending_stack, core_op.text())
                return
        fence_attrs = {'open': core_op.text(), 'close': '', 'separators': ''}
        pending_stack.append(Pending(MFenced(fence_attrs)))
    else:
        pending_stack[-1].append(elem)

def merge_mrow_elems(elements):
    last_idx = len(elements) - 1
    for idx in range(last_idx, -1, -1):
        if not elements[idx].is_space_like():
            last_idx = idx
            break
    else:
        return elements
    first_idx = 0
    for idx in range(first_idx, last_idx):
        if not elements[idx].is_space_like():
            first_idx = idx
            break
    else:
        return elements

    new_elements = []
    pending_stack = [new_elements]
    _append_elem(pending_stack, elements[first_idx], 'prefix')
    for elem in elements[first_idx + 1:last_idx]:
        _append_elem(pending_stack, elem, 'infix')
    _append_elem(pending_stack, elements[last_idx], 'postfix')

    while len(pending_stack) != 1:
        pending = pending_stack.pop()
        pending_stack[-1].append(pending.fix())
    return elements[0:first_idx] + new_elements + elements[last_idx+1:]

def make_script_style_props(attrs, default_style='normal'):
    script_list = [
        'script', 'fraktur', 'sans-serif', 'monospace', 'double-struck', 'roman'
    ]
    style_map = {
        'bold-italic': 'bi', 'bold': 'b', 'italic': 'i', 'normal': 'p',
    }

    variant = attrs.get('mathvariant')
    if variant is None:
        return ['<m:sty m:val="%s"/>' % style_map[default_style]]

    props = []
    for script in script_list:
        if variant.find(script) != -1:
            props.append('<m:scr m:val="%s"/>' % script)
            break
    for style, val in style_map.items():
        if variant.find(style) != -1:
            props.append('<m:sty m:val="%s"/>' % val)
            break
    else:
        props.append('<m:sty m:val="%s"/>' % style_map[default_style])
    return props

def is_stretch_accent(operator):
    attrs = op_attrs(operator)
    return attrs['stretchy'] and attrs['accent']

class Run:
    def __init__(self, attrs):
        self.children = []
        self.attrs = attrs

    def set_text(self, text):
        self.children.append(text)

    def text(self):
        return ''.join(self.children)

    def escape_text(self):
        return xml.sax.saxutils.escape(
            re.sub(INVISIBLE_CHAR_PATTERN, '', self.text()))

    def __str__(self):
        text = self.escape_text()
        props = self.props()
        if props:
            run_prop = '<m:rPr>%s</m:rPr>' % ''.join(props)
        else:
            run_prop = ''
        return '<m:r>%s<m:t>%s</m:t></m:r>' % (run_prop, text)

    def props(self): # pylint: disable=no-self-use
        return []

class FixedArgumentElement:
    name = ''
    expected_num_args = 0

    def __init__(self, attrs):
        self.children = []
        self.attrs = attrs

    def append(self, child):
        if len(self.children) == self.expected_num_args:
            raise RuntimeError('Too large number of children for ' + self.name)
        self.children.append(child)

    def __str__(self):
        if len(self.children) < self.expected_num_args:
            raise RuntimeError('Too small number of children for ' + self.name)
        return self.to_str()

    def to_str(self):
        pass

class NaryableElement:
    name = ''
    num_args = 4
    num_nary_args = 4
    default_script_location = 'subSup'

    def __init__(self, attrs, ):
        self.children = []
        self.attrs = attrs

    def __str__(self):
        num_children = len(self.children)
        if num_children not in (self.num_args, self.num_nary_args):
            raise RuntimeError('Too small number of children for ' + self.name)
        if not (len(self.children) == self.num_nary_args and self.is_nary()):
            return self.to_str()
        # pylint: disable=unbalanced-tuple-unpacking
        base, sub, sup, elem = self.nary_elems()
        base = base.escape_text()
        sub = to_math_arg(sub)
        sup = to_math_arg(sup)
        elem = to_element(elem)
        return ('<m:nary>'
                '<m:naryPr>'
                '<m:chr m:val="%s"/>'
                '<m:limLoc m:val="%s"/>'
                '</m:naryPr>'
                '<m:sub>%s</m:sub>'
                '<m:sup>%s</m:sup>'
                '%s'
                '</m:nary>') % (base, self.script_location(), sub, sup, elem)

    def append(self, child):
        if len(self.children) == self._max_num_args():
            raise RuntimeError('Too large number of children for ' + self.name)
        self.children.append(child)

    def is_nary(self):
        if not self.children:
            return False
        if not isinstance(self.children[0], MO):
            return False
        attrs = op_attrs(self.children[0])
        return attrs['largeop'] and attrs['form'] == 'prefix'

    def nary_elems(self):
        return self.children

    def script_location(self):
        attrs = op_attrs(self.children[0])
        if attrs['movablelimits']:
            return 'undOvr'
        return self.default_script_location

    def to_str(self):
        pass

    def _max_num_args(self):
        if self.is_nary():
            return max(self.num_args, self.num_nary_args)
        return self.num_args

class InferredMRowElement:
    def __init__(self, attrs):
        self.mrow = MRow({})
        self.attrs = attrs

    def __str__(self):
        return self.to_str()

    def append(self, child):
        self.mrow.append(child)

    def to_str(self):
        pass

    def merge_children(self):
        self.mrow.merge_children()


class MI(Run):
    """Identifier.
    <mi>
    """
    name = 'mi'

    def props(self):
        default = 'italic' if len(self.text().strip()) == 1 else 'normal'
        return make_script_style_props(self.attrs, default_style=default)

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

class MN(Run):
    """Number.
    <mi>
    """
    name = 'mn'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def props(self):
        return make_script_style_props(self.attrs)

class MO(Run):
    """Operator, Fence, Separator or Accent.
    <mo>
    """
    name = 'mo'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return self

    def props(self):
        return make_script_style_props(self.attrs)

class MText(Run):
    """Text.
    <mtext>
    """
    name = 'mtext'

    def is_space_like(self): # pylint: disable=no-self-use
        return True

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def props(self):
        variant = self.attrs.get('mathvariant')
        if variant is None or variant == 'normal':
            return ['<m:nor/>']
        return make_script_style_props(self.attrs)

class MSpace(Run): # TODO
    """Space
    """
    name = 'mspace'

    def is_space_like(self): # pylint: disable=no-self-use
        return True

    def embellished_op(self): # pylint: disable=no-self-use
        return None

class MS(Run):
    """String Literal.
    """
    name = 'ms'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def text(self):
        lquote = self.attrs.get('lquote', '"')
        rquote = self.attrs.get('rquote', '"')
        return lquote + ''.join(self.children) + rquote

    def props(self):
        variant = self.attrs.get('mathvariant')
        if variant is None or variant == 'normal':
            return ['<m:nor/>']
        return make_script_style_props(self.attrs)

class Math(InferredMRowElement):
    """Top-Level Element.
    <math> any* </math>

    <m:oMath>
        (acc|bar|box|borderBox|d|eqArr|f|func|groupChr
        |limLow|limUpp|m|nary|phant|rad|sPre|sSub|sSubSup|sSup|r)*
    </m:oMath>
    """
    name = 'math'

    def to_str(self):
        xml_text = ''.join(to_box(c) for c in self.mrow.children)
        return '<m:oMath>%s</m:oMath>' % xml_text

class MRow:
    """Horizontally Group Sub-Expressions.
    <mrow> * </mrow>

    <m:e>
        argPr?
        (acc|bar|box|borderBox|d|eqArr|f|func|groupChr
        |limLow|limUpp|m|nary|phant|rad|sPre|sSub|sSubSup|sSup|r)*
        ctrlPr?
    </m:e>
    """
    name = 'mrow'

    def __init__(self, attrs):
        self.children = []
        self.attrs = attrs

    def __str__(self):
        return '<m:box>%s</m:box>' % Element(*self.children)

    def append(self, child):
        self.children.append(child)

    def is_space_like(self):
        return all((c.is_space_like() for c in self.children))

    def embellished_op(self):
        first_embellished = None
        for child in self.children:
            if child.is_space_like():
                continue
            embellished = child.embellished_op()
            if embellished is None or first_embellished is not None:
                return None
            first_embellished = child
        return first_embellished

    def merge_children(self):
        self.children = merge_mrow_elems(self.children)

class MSqrt(InferredMRowElement):
    """Radical.
    <msqrt> base:inferred_mrow </msqrt>

    <m:rad> radPr e </m:rad>
    """
    name = 'msqrt'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def to_str(self):
        return '<m:rad>%s</m:rad>' % to_element(self.mrow)

class MRoot(FixedArgumentElement):
    """Radical.
    <mroot> base index </mroot>

    <m:rad> radPr deg:oMathArg e </m:drad>
    """
    name = 'mroot'
    expected_num_args = 2

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def to_str(self):
        base = to_element(self.children[0])
        deg = to_math_arg(self.children[1])
        return '<m:rad><m:deg>%s</m:deg>%s</m:rad>' % (deg, base)

class MFrac(FixedArgumentElement):
    """Fractions
    <mfrac> numerator denominator </mfrac>

    <m:f> fPr num:oMathArg den:oMathArg </mf>
    """
    name = 'mfrac'
    expected_num_args = 2

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def to_str(self):
        num = to_math_arg(self.children[0])
        den = to_math_arg(self.children[1])
        return ('<m:f>'
                '%s<m:num>%s</m:num><m:den>%s</m:den>'
                '</m:f>') % (self._props(), num, den)

    def _props(self):
        thickness = self.attrs.get('linethickness')
        if thickness and re.match(r'^0[^0-9.]+$', thickness.strip()):
            return '<m:fPr><m:type m:val="noBar"/></m:fPr>'
        if self.attrs.get('bevelled') == 'true':
            return '<m:fPr><m:type m:val="skw"/></m:fPr>'
        return ''

class MPadded(InferredMRowElement):
    """Adjust Space Around Content.
    <mpadded> elem:inferred_mrow </mpadded>
    """
    name = 'mpadded'

    def is_space_like(self):
        return self.mrow.is_space_like()

    def embellished_op(self):
        return self.mrow.embellished_op()

    def to_str(self):
        return str(self.mrow) # TODO

class MStyle(InferredMRowElement):
    """Style Change.
    <mstyle> elem:inferred_mrow </mstyle>
    """
    name = 'mstyle'

    def is_space_like(self):
        return self.mrow.is_space_like()

    def embellished_op(self):
        return self.mrow.embellished_op()

    def to_str(self):
        return str(self.mrow) # TODO

class MPhantom(InferredMRowElement):
    """Making Sub-Expressions Invisible.
    <mphantom> elem:inferred_mrow </mphantom>

    <m:phant> phantPr e </m:phant>
    """
    name = 'mphantom'

    def is_space_like(self):
        return self.mrow.is_space_like()

    def embellished_op(self):
        return self

    def to_str(self):
        return ('<m:phant>'
                '<m:phantPr><m:show m:val="0"/></m:phantPr>'
                '%s'
                '</m:phant>') % to_element(self.mrow)

class MFenced:
    """Expression Inside Pair of Fences.
    <mfenced> elem* </mfenced>

    <m:d> dPr e* </m:d>
    """
    name = 'mfenced'

    def __init__(self, attrs):
        self.children = []
        self.attrs = attrs

    def __str__(self):
        seps = self.attrs.get('separators', ',').replace(' ', '')
        if len(self.children) > 1 and seps:
            elem = Element(self.children[0])
            for idx, child in enumerate(self.children[1:]):
                run = Run({})
                run.set_text(seps[idx] if idx < len(seps) else seps[-1])
                elem.append(run)
                elem.append(child)
        else:
            elem = Element(*self.children)
        beg_chr = xml.sax.saxutils.escape(self.attrs.get('open', '('))
        end_chr = xml.sax.saxutils.escape(self.attrs.get('close', ')'))
        return ('<m:d>'
                '<m:dPr>'
                '<m:begChr m:val="%s"/>'
                '<m:endChr m:val="%s"/>'
                '</m:dPr>'
                '%s'
                '</m:d>') % (beg_chr, end_chr, elem)

    def append(self, child):
        self.children.append(child)

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

class MEnclose(InferredMRowElement):
    """Enclose Expression Inside Notation.
    <menclose> elem:inferred_mrow </menclose>

    <m:borderBox> borderBoxPr e </m:borderBox>
    """
    name = 'menclose'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def to_str(self): # TODO borderBoxPr
        return ('<m:borderBox>'
                '%s'
                '</m:borderBox>') % to_element(self.mrow)

class MSub(NaryableElement):
    """Subscript.
    <msub> base subscript </msub>

    <m:nary> naryPr sub:oMathArg e </m:nary>
    <m:sSub> sSubPr e sub:oMathArg </m:sSub>
    """
    name = 'msub'
    num_args = 2
    num_nary_args = 3

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def nary_elems(self):
        return (self.children[0], self.children[1], Element(), self.children[2])

    def to_str(self):
        base = to_element(self.children[0])
        sub = to_math_arg(self.children[1])
        return '<m:sSub>%s<m:sub>%s</m:sub></m:sSub>' % (base, sub)

class MSup(NaryableElement):
    """Superscript.
    <msup> base superscript </msup>

    <m:nary> naryPr sup:oMathArg e </m:nary>
    <m:sSup> sSupPr e sup:oMathArg </m:sSup>
    """
    name = 'msup'
    num_args = 2
    num_nary_args = 3

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def nary_elems(self):
        return (self.children[0], Element(), self.children[1], self.children[2])

    def to_str(self):
        base = to_element(self.children[0])
        sup = to_math_arg(self.children[1])
        return '<m:sSup>%s<m:sup>%s</m:sup></m:sSup>' % (base, sup)

class MSubSup(NaryableElement):
    """Subscript-superscript Pair.
    <msubsup> base subscript superscript </msubsup>

    <m:nary> naryPr sub:oMathArg sup:oMathArg e </m:nary>
    <m:sSubSup> sSubSupPr e sub:oMathArg sup:oMathArg </m:sSubSup>
    """
    name = 'msubsup'
    num_args = 3
    num_nary_args = 4

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def nary_elems(self):
        return self.children

    def to_str(self):
        base = to_element(self.children[0])
        sub = to_math_arg(self.children[1])
        sup = to_math_arg(self.children[2])
        return ('<m:sSubSup>'
                '%s'
                '<m:sub>%s</m:sub>'
                '<m:sup>%s</m:sup>'
                '</m:sSubSup>') % (base, sub, sup)

class MUnder(NaryableElement):
    """Underscript
    <munder> base underscript </munder>

    <m:limLow> limLowPr e lim:oMathArg </m:limLow>
    <m:groupChr> groupChrPr e </m:groupChr>
    <m:nary> naryPr sub:oMathArg e </m:nary>
    """
    name = 'munder'
    num_args = 2
    num_nary_args = 3
    default_script_location = 'undOvr'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def nary_elems(self):
        return (self.children[0], self.children[1], Element(), self.children[2])

    def to_str(self):
        base = to_element(self.children[0])
        underscript = self.children[1]
        if isinstance(underscript, MO) and is_stretch_accent(underscript):
            return ('<m:groupChr>'
                    '<m:groupChrPr>'
                    '<m:chr m:val="%s"/>'
                    '<m:pos m:val="bot"/>'
                    '</m:groupChr>'
                    '%s'
                    '</m:groupChr>') % (underscript.escape_text(), base)
        return ('<m:limLow>'
                '%s'
                '<m:lim>%s</m:lim>'
                '</m:limLow>') % (base, to_math_arg(underscript))

class MOver(NaryableElement):
    """Overscript
    <mover> base overscript </mover>

    <m:limUpp> limUppPr e lim:oMathArg </m:limUpp>
    <m:nary> naryPr sup:oMathArg e </m:nary>
    """
    name = 'mover'
    num_args = 2
    num_nary_args = 3
    default_script_location = 'undOvr'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def nary_elems(self):
        return (self.children[0], Element(), self.children[1], self.children[2])

    def to_str(self):
        base = to_element(self.children[0])
        overscript = self.children[1]
        if isinstance(overscript, MO) and is_stretch_accent(overscript):
            return ('<m:groupChr>'
                    '<m:groupChrPr>'
                    '<m:chr m:val="%s"/>'
                    '<m:pos m:val="top"/>'
                    '</m:groupChr>'
                    '%s'
                    '</m:groupChr>') % (overscript.escape_text(), base)
        return ('<m:limUpp>'
                '%s'
                '<m:lim>%s</m:lim>'
                '</m:limUpp>') % (base, to_math_arg(overscript))

class MUnderOver(NaryableElement):
    """Underscript-overscript Pair.
    <munderover> base underscript overscript </munderover>

    <m:nary> naryPr sub:oMathArg sup:oMathArg e </m:nary>
    """
    name = 'munderover'
    num_args = 3
    num_nary_args = 4
    default_script_location = 'undOvr'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

    def nary_elems(self):
        return self.children

    def to_str(self):
        base = to_element(self.children[0])
        underscript = to_math_arg(self.children[1])
        overscript = to_math_arg(self.children[2])
        return ('<m:limLow>'
                '<m:e>'
                '<m:limUpp>'
                '%s'
                '<m:lim>%s</m:lim>'
                '</m:limUpp>'
                '</m:e>'
                '<m:lim>%s</m:lim>'
                '</m:limLow>') % (base, overscript, underscript)

class MPreScripts:
    """
    <mprescripts/>
    """
    name = 'mprescripts'

    def __init__(self, _attrs):
        pass

    def __str__(self):
        return ''

    def append(self, child):
        raise RuntimeError('This method is never called for ' + self.name)

class MNone:
    """
    <none/>
    """
    name = 'none'

    def __init__(self, _attrs):
        pass

    def __str__(self):
        return ''

    def append(self, child):
        raise RuntimeError('This method is never called for ' + self.name)

class MMultiScripts:
    """Prescripts and Tensor Indices.
    <mmultiscripts>
        base (subscript superscript)*
        [ <mprescripts/> (presubscript presuperscript)* ]
    </mmultiscripts>

    <m:sPre> sub:oMathArg sup:oMathArg e:<sSubSup> </m:sPre>
    """
    name = 'mmultiscripts'

    def __init__(self, _attrs):
        self.children = []
        self.prescripts = None

    def __str__(self):
        if not self.children:
            raise RuntimeError('Too small number of children for ' + self.name)
        if len(self.children) % 2 != 1:
            raise RuntimeError(
                'The number of postscripts must be even for ' + self.name)
        if self.prescripts is not None and len(self.prescripts) % 2 != 0:
            raise RuntimeError(
                'The number of prescripts must be even for ' + self.name)
        base = self.children[0]
        for idx in range(1, len(self.children), 2):
            postsub = to_math_arg(self.children[idx])
            postsup = to_math_arg(self.children[idx + 1])
            base = ('<m:sSubSup>'
                    '%s'
                    '<m:sub>%s</m:sub>'
                    '<m:sup>%s</m:sup>'
                    '</m:sSubSup>') % (to_element(base), postsub, postsup)
        if self.prescripts is None:
            return '<m:sPre>%s</m:sPre>' % to_element(base)
        for idx in range(len(self.prescripts), 0, -2):
            presub = to_math_arg(self.prescripts[idx - 2])
            presup = to_math_arg(self.prescripts[idx - 1])
            base = ('<m:sPre>'
                    '<m:sub>%s</m:sub>'
                    '<m:sup>%s</m:sup>'
                    '%s'
                    '</m:sPre>') % (presub, presup, to_element(base))
        return base

    def append(self, child):
        if isinstance(child, MPreScripts):
            if self.prescripts is not None:
                raise RuntimeError(
                    'The number of mprescripts must be 1 for ' + self.name)
            self.prescripts = []
            return
        if self.prescripts is not None:
            self.prescripts.append(child)
        else:
            self.children.append(child)

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self):
        return self

class MTable:
    """Table or Matrix
    <mtable> (<mtr>|<mlabeledtr>)* </mtable>

    <m:m> mPr mr* </m:m>
    """
    name = 'mtable'

    def __init__(self, _attrs):
        self.children = []

    def __str__(self):
        columns = max((len(row.children) for row in self.children), default=0)
        rows = (MTableRow(
            row.attrs, *row.children,
            *itertools.repeat(MTableData({}), columns - len(row.children)))
                for row in self.children)
        return '<m:m>%s</m:m>' % ''.join(str(row) for row in rows)

    def append(self, child):
        if not isinstance(child, MTableRow):
            raise RuntimeError('Child must be mtr for ' + self.name)
        self.children.append(child)

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

class MTableRow:
    """Raw in Table or Matrix.
    <mtr> <mtd>* </mtr>

    <m:mr> e* </m:mr>
    """
    name = 'mtr'

    def __init__(self, attrs, *children):
        self.attrs = attrs
        self.children = list(children)

    def __str__(self):
        return '<m:mr>%s</m:mr>' % ''.join(to_element(c) for c in self.children)

    def append(self, child):
        if not isinstance(child, MTableData):
            raise RuntimeError('Child must be mtd for ' + self.name)
        self.children.append(child)

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

class MTableData(InferredMRowElement):
    """Entry in Table or Matrix.
    <mtd> elem:inferred_mrow </mtd>
    """
    name = 'mtd'

    def is_space_like(self): # pylint: disable=no-self-use
        return False

    def embellished_op(self): # pylint: disable=no-self-use
        return None

    def to_str(self):
        return str(self.mrow)

class MAction:
    """Bind Action to Sub-Expression
    <maction actiontype> expressoins </maction>
    """
    name = "maction"
    num_args_map = {
        'statusline': 2,
        'tooltip': 2,
        'input': 1,
    }

    def __init__(self, attrs):
        self.children = []
        self.attrs = attrs
        if attrs.get('actiontype') is None:
            raise RuntimeError(self.name + ' must have actiontype')

    def __str__(self):
        return str(self._selected_exp())

    def append(self, child):
        num_args = self.num_args_map.get(self.attrs['actiontype'])
        if num_args is not None and len(self.children) == num_args:
            raise RuntimeError('Too large number of children for ' + self.name)
        self.children.append(child)

    def is_space_like(self):
        return self._selected_exp().is_space_like()

    def embellished_op(self):
        return self._selected_exp().embellished_op()

    def _selected_exp(self):
        if self.attrs['actiontype'] == 'toggle':
            idx = int(self.attrs.get('selection', '1')) - 1
        else:
            idx = 0
        return self.children[idx]

class MathMLHandler(xml.sax.handler.ContentHandler):
    CONVERSION_MAP = dict((cls.name, cls) for cls in (
        MI, MN, MO, MText, MSpace, MS,
        Math, MRow,
        MSqrt, MRoot,
        MFrac,
        MStyle, MPadded, MPhantom,
        MFenced, MEnclose,
        MSub, MSup, MSubSup,
        MUnder, MOver, MUnderOver,
        MMultiScripts, MPreScripts, MNone,
        MTable, MTableRow, MTableData,
        MAction,
        ))
    IGNORED_ELEMENTS = ('annotation-xml', 'annotation')
    SKIPPED_ELEMENTS = ('semantics',)

    def __init__(self):
        super(MathMLHandler, self).__init__()
        self._stack = []
        self._stack.append([])
        self._in_ignore_elems = 0

    def startElement(self, name, attrs):
        if name in MathMLHandler.IGNORED_ELEMENTS:
            self._in_ignore_elems += 1
            return
        if self._in_ignore_elems > 0 or name in MathMLHandler.SKIPPED_ELEMENTS:
            return
        if name not in MathMLHandler.CONVERSION_MAP:
            raise NotImplementedError(name + ' is not Implemented')
        self._stack.append(MathMLHandler.CONVERSION_MAP[name](attrs))

    def endElement(self, name):
        if name in MathMLHandler.IGNORED_ELEMENTS:
            self._in_ignore_elems -= 1
            return
        if self._in_ignore_elems > 0 or name in MathMLHandler.SKIPPED_ELEMENTS:
            return
        elem = self._stack.pop()
        if isinstance(elem, (MRow, InferredMRowElement)):
            elem.merge_children()
        self._stack[-1].append(elem)

    def characters(self, content):
        if hasattr(self._stack[-1], 'set_text'):
            self._stack[-1].set_text(content)
        else:
            if content.strip() != '':
                print(content)

    def result(self):
        return str(self._stack[-1][0])

def convert(mathml_xml, additional_entities=None):
    """Convert MathML text to OMML text
    """
    handler = MathMLHandler()
    entities = {
        'pi': 0x03c0,
        'ExponentialE': 0x2147,
        'ee': 0x2147,
        'ImaginaryI': 0x2148,
        'ii': 0x2148,
        'gamma': 0x03b3,
        'infin': 0x221e,
        'infty': 0x221e,
    }
    if additional_entities is not None:
        entities.update(additional_entities)
    input_xml = (
        r"""<!DOCTYPE math [ """ +
        ''.join('<!ENTITY %s "&#x%04X;">' % item for item in entities.items()) +
        r""" ]>""" +
        mathml_xml)
    xml.sax.parseString(input_xml, handler)
    return handler.result()
