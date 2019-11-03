#!/usr/bin/env python3
# pylint: disable=missing-docstring
import unittest
import mathml2omml # pylint: disable=import-error

class ConvertTest(unittest.TestCase):
    def test_identifiers1(self):
        mathml = '<math><mrow><mi>x</mi></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>x</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_identifiers2(self):
        mathml = '<math><mrow><mi>x</mi><mi>y</mi><mi>z</mi></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>x</m:t></m:r>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>y</m:t></m:r>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>z</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_identifiers3(self):
        mathml = '<math><mrow><mi>xyz</mi></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>xyz</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_numbers1(self):
        mathml = '<math><mrow><mn>3</mn></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>3</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_numbers2(self):
        mathml = '<math><mrow><mn>444</mn></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>444</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_numbers3(self):
        mathml = '<math><mrow><mn>12.34</mn></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>12.34</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_identifier_and_numbers(self):
        mathml = '<math><mrow><mn>12</mn><mi>x</mi></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>12</m:t></m:r>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>x</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_operator(self):
        mathml = '<math><mrow><mn>3</mn><mo>-</mo><mn>2</mn></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>3</m:t></m:r>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>-</m:t></m:r>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>2</m:t></m:r>'
            '</m:e></m:box></m:oMath>')

    def test_subscript(self):
        mathml = '<math><mrow><msub><mi>a</mi><mi>b</mi></msub></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:sSub>'
            '<m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r>'
            '</m:e>'
            '<m:sub>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>b</m:t></m:r>'
            '</m:sub>'
            '</m:sSub></m:e></m:box></m:oMath>')

    def test_superscript(self):
        mathml = '<math><mrow><msup><mi>a</mi><mi>b</mi></msup></mrow></math>'

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:sSup>'
            '<m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r>'
            '</m:e>'
            '<m:sup>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>b</m:t></m:r>'
            '</m:sup>'
            '</m:sSup></m:e></m:box></m:oMath>')

    def test_subsuperscript(self):
        mathml = (
            '<math><mrow>'
            '<msubsup><mi>a</mi><mi>b</mi><mi>c</mi></msubsup>'
            '</mrow></math>')

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:sSubSup>'
            '<m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r>'
            '</m:e>'
            '<m:sub>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>b</m:t></m:r>'
            '</m:sub>'
            '<m:sup>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>c</m:t></m:r>'
            '</m:sup>'
            '</m:sSubSup></m:e></m:box></m:oMath>')

    def test_fraction(self):
        mathml = (
            '<math><mrow>'
            '<mfrac><mrow><mn>1</mn></mrow><mrow><mn>2</mn></mrow></mfrac>'
            '</mrow></math>')

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:f>'
            '<m:num><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>1</m:t></m:r>'
            '</m:e></m:box></m:num>'
            '<m:den><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>2</m:t></m:r>'
            '</m:e></m:box></m:den>'
            '</m:f></m:e></m:box></m:oMath>')

    def test_sqrt(self):
        mathml = (
            '<math><mrow>'
            '<msqrt><mrow><mn>2</mn></mrow></msqrt>'
            '</mrow></math>')

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:rad>'
            '<m:e><m:box><m:e><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>2</m:t></m:r>'
            '</m:e></m:box></m:e></m:box></m:e>'
            '</m:rad></m:e></m:box></m:oMath>')

    def test_root(self):
        mathml = (
            '<math><mrow>'
            '<mroot><mrow><mn>2</mn></mrow><mrow><mn>3</mn></mrow></mroot>'
            '</mrow></math>')

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:rad>'
            '<m:deg><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>3</m:t></m:r>'
            '</m:e></m:box></m:deg>'
            '<m:e><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>2</m:t></m:r>'
            '</m:e></m:box></m:e>'
            '</m:rad></m:e></m:box></m:oMath>')

    def test_matrix1(self):
        mathml = (
            '<math><mrow><mtable>'
            '<mtr><mtd><mi>a</mi></mtd><mtd><mi>b</mi></mtd></mtr>'
            '<mtr><mtd><mi>c</mi></mtd><mtd><mi>d</mi></mtd></mtr>'
            '</mtable></mrow></math>')

        result = mathml2omml.convert(mathml)

        self.assertEqual(
            result,
            '<m:oMath><m:box><m:e><m:m>'
            '<m:mr>'
            '<m:e><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r>'
            '</m:e></m:box></m:e>'
            '<m:e><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>b</m:t></m:r>'
            '</m:e></m:box></m:e>'
            '</m:mr>'
            '<m:mr>'
            '<m:e><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>c</m:t></m:r>'
            '</m:e></m:box></m:e>'
            '<m:e><m:box><m:e>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>d</m:t></m:r>'
            '</m:e></m:box></m:e>'
            '</m:mr>'
            '</m:m></m:e></m:box></m:oMath>')
