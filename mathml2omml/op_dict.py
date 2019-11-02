# pylint: disable=missing-docstring, line-too-long, too-many-lines

# Operator Dictionay: See https://www.w3.org/TR/MathML3/appendixc.html
OP_DICT = {
    ('\u2018', 'prefix'): {'priority': 10, 'lspace': 0, 'rspace': 0, 'fence': True, }, # ‘ left single quotation mark
    ('\u2019', 'postfix'): {'priority': 10, 'lspace': 0, 'rspace': 0, 'fence': True, }, # ’ right single quotation mark
    ('\u201C', 'prefix'): {'priority': 10, 'lspace': 0, 'rspace': 0, 'fence': True, }, # “ left double quotation mark
    ('\u201D', 'postfix'): {'priority': 10, 'lspace': 0, 'rspace': 0, 'fence': True, }, # ” right double quotation mark
    ('(', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ( left parenthesis
    (')', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ) right parenthesis
    ('[', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # [ left square bracket
    (']', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ] right square bracket
    ('{', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # { left curly bracket
    ('|', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # | vertical line
    ('|', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # | vertical line
    ('||', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # || multiple character operator: ||
    ('||', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # || multiple character operator: ||
    ('|||', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ||| multiple character operator: |||
    ('|||', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ||| multiple character operator: |||
    ('}', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # } right curly bracket
    ('\u2016', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, }, # ‖ double vertical line
    ('\u2016', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, }, # ‖ double vertical line
    ('\u2308', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⌈ left ceiling
    ('\u2309', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⌉ right ceiling
    ('\u230A', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⌊ left floor
    ('\u230B', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⌋ right floor
    ('\u2329', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # 〈 left-pointing angle bracket
    ('\u232A', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # 〉 right-pointing angle bracket
    ('\u2772', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ❲ light left tortoise shell bracket ornament
    ('\u2773', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ❳ light right tortoise shell bracket ornament
    ('\u27E6', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟦ mathematical left white square bracket
    ('\u27E7', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟧ mathematical right white square bracket
    ('\u27E8', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟨ mathematical left angle bracket
    ('\u27E9', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟩ mathematical right angle bracket
    ('\u27EA', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟪ mathematical left double angle bracket
    ('\u27EB', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟫ mathematical right double angle bracket
    ('\u27EC', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟬ mathematical left white tortoise shell bracket
    ('\u27ED', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟭ mathematical right white tortoise shell bracket
    ('\u27EE', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟮ mathematical left flattened parenthesis
    ('\u27EF', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⟯ mathematical right flattened parenthesis
    ('\u2980', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, }, # ⦀ triple vertical bar delimiter
    ('\u2980', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, }, # ⦀ triple vertical bar delimiter
    ('\u2983', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦃ left white curly bracket
    ('\u2984', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦄ right white curly bracket
    ('\u2985', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦅ left white parenthesis
    ('\u2986', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦆ right white parenthesis
    ('\u2987', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦇ z notation left image bracket
    ('\u2988', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦈ z notation right image bracket
    ('\u2989', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦉ z notation left binding bracket
    ('\u298A', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦊ z notation right binding bracket
    ('\u298B', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦋ left square bracket with underbar
    ('\u298C', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦌ right square bracket with underbar
    ('\u298D', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦍ left square bracket with tick in top corner
    ('\u298E', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦎ right square bracket with tick in bottom corner
    ('\u298F', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦏ left square bracket with tick in bottom corner
    ('\u2990', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦐ right square bracket with tick in top corner
    ('\u2991', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦑ left angle bracket with dot
    ('\u2992', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦒ right angle bracket with dot
    ('\u2993', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦓ left arc less-than bracket
    ('\u2994', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦔ right arc greater-than bracket
    ('\u2995', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦕ double left arc greater-than bracket
    ('\u2996', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦖ double right arc less-than bracket
    ('\u2997', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦗ left black tortoise shell bracket
    ('\u2998', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⦘ right black tortoise shell bracket
    ('\u29FC', 'prefix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⧼ left-pointing curved angle bracket
    ('\u29FD', 'postfix'): {'priority': 20, 'lspace': 0, 'rspace': 0, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ⧽ right-pointing curved angle bracket
    (';', 'infix'): {'priority': 30, 'lspace': 0, 'rspace': 3, 'separator': True, 'linebreakstyle': 'after', }, # ; semicolon
    (', ', 'infix'): {'priority': 40, 'lspace': 0, 'rspace': 3, 'separator': True, 'linebreakstyle': 'after', }, # , comma
    ('\u2063', 'infix'): {'priority': 40, 'lspace': 0, 'rspace': 0, 'separator': True, 'linebreakstyle': 'after', }, # ⁣ invisible separator
    ('\u2234', 'infix'): {'priority': 70, 'lspace': 5, 'rspace': 5, }, # ∴ therefore
    ('\u2235', 'infix'): {'priority': 70, 'lspace': 5, 'rspace': 5, }, # ∵ because
    ('->', 'infix'): {'priority': 90, 'lspace': 5, 'rspace': 5, }, # -> multiple character operator: ->
    ('..', 'postfix'): {'priority': 100, 'lspace': 0, 'rspace': 0, }, # .. multiple character operator: ..
    ('...', 'postfix'): {'priority': 100, 'lspace': 0, 'rspace': 0, }, # ... multiple character operator: ...
    (':', 'infix'): {'priority': 100, 'lspace': 1, 'rspace': 2, }, # : colon
    ('\u03F6', 'infix'): {'priority': 110, 'lspace': 5, 'rspace': 5, }, # ϶ greek reversed lunate epsilon symbol
    ('\u2026', 'infix'): {'priority': 150, 'lspace': 0, 'rspace': 0, }, # … horizontal ellipsis
    ('\u22EE', 'infix'): {'priority': 150, 'lspace': 5, 'rspace': 5, }, # ⋮ vertical ellipsis
    ('\u22EF', 'infix'): {'priority': 150, 'lspace': 0, 'rspace': 0, }, # ⋯ midline horizontal ellipsis
    ('\u22F1', 'infix'): {'priority': 150, 'lspace': 5, 'rspace': 5, }, # ⋱ down right diagonal ellipsis
    ('\u220B', 'infix'): {'priority': 160, 'lspace': 5, 'rspace': 5, }, # ∋ contains as member
    ('\u22A2', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊢ right tack
    ('\u22A3', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊣ left tack
    ('\u22A4', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊤ down tack
    ('\u22A8', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊨ true
    ('\u22A9', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊩ forces
    ('\u22AC', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊬ does not prove
    ('\u22AD', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊭ not true
    ('\u22AE', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊮ does not force
    ('\u22AF', 'infix'): {'priority': 170, 'lspace': 5, 'rspace': 5, }, # ⊯ negated double vertical bar double right turnstile
    ('\u2228', 'infix'): {'priority': 190, 'lspace': 4, 'rspace': 4, }, # ∨ logical or
    ('&&', 'infix'): {'priority': 200, 'lspace': 4, 'rspace': 4, }, # && multiple character operator: &&
    ('\u2227', 'infix'): {'priority': 200, 'lspace': 4, 'rspace': 4, }, # ∧ logical and
    ('\u2200', 'prefix'): {'priority': 230, 'lspace': 2, 'rspace': 1, }, # ∀ for all
    ('\u2203', 'prefix'): {'priority': 230, 'lspace': 2, 'rspace': 1, }, # ∃ there exists
    ('\u2204', 'prefix'): {'priority': 230, 'lspace': 2, 'rspace': 1, }, # ∄ there does not exist
    ('\u2201', 'infix'): {'priority': 240, 'lspace': 1, 'rspace': 2, }, # ∁ complement
    ('\u2208', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ∈ element of
    ('\u2209', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ∉ not an element of
    ('\u220C', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ∌ does not contain as member
    ('\u2282', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊂ subset of
    ('\u2282\u20D2', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊂⃒ subset of with vertical line
    ('\u2283', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊃ superset of
    ('\u2283\u20D2', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊃⃒ superset of with vertical line
    ('\u2284', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊄ not a subset of
    ('\u2285', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊅ not a superset of
    ('\u2286', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊆ subset of or equal to
    ('\u2287', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊇ superset of or equal to
    ('\u2288', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊈ neither a subset of nor equal to
    ('\u2289', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊉ neither a superset of nor equal to
    ('\u228A', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊊ subset of with not equal to
    ('\u228B', 'infix'): {'priority': 240, 'lspace': 5, 'rspace': 5, }, # ⊋ superset of with not equal to
    ('<=', 'infix'): {'priority': 241, 'lspace': 5, 'rspace': 5, }, # <= multiple character operator: <=
    ('\u2264', 'infix'): {'priority': 241, 'lspace': 5, 'rspace': 5, }, # ≤ less-than or equal to
    ('\u2265', 'infix'): {'priority': 242, 'lspace': 5, 'rspace': 5, }, # ≥ greater-than or equal to
    ('>', 'infix'): {'priority': 243, 'lspace': 5, 'rspace': 5, }, # > greater-than sign
    ('>=', 'infix'): {'priority': 243, 'lspace': 5, 'rspace': 5, }, # >= multiple character operator: >=
    ('\u226F', 'infix'): {'priority': 244, 'lspace': 5, 'rspace': 5, }, # ≯ not greater-than
    ('<', 'infix'): {'priority': 245, 'lspace': 5, 'rspace': 5, }, # < less-than sign
    ('\u226E', 'infix'): {'priority': 246, 'lspace': 5, 'rspace': 5, }, # ≮ not less-than
    ('\u2248', 'infix'): {'priority': 247, 'lspace': 5, 'rspace': 5, }, # ≈ almost equal to
    ('\u223C', 'infix'): {'priority': 250, 'lspace': 5, 'rspace': 5, }, # ∼ tilde operator
    ('\u2249', 'infix'): {'priority': 250, 'lspace': 5, 'rspace': 5, }, # ≉ not almost equal to
    ('\u2262', 'infix'): {'priority': 252, 'lspace': 5, 'rspace': 5, }, # ≢ not identical to
    ('\u2260', 'infix'): {'priority': 255, 'lspace': 5, 'rspace': 5, }, # ≠ not equal to
    ('!=', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # != multiple character operator: !=
    ('*=', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # *= multiple character operator: *=
    ('+=', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # += multiple character operator: +=
    ('-=', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # -= multiple character operator: -=
    ('/=', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # /= multiple character operator: /=
    (':=', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # := multiple character operator: :=
    ('=', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # = equals sign
    ('==', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # == multiple character operator: ==
    ('\u221D', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ∝ proportional to
    ('\u2224', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ∤ does not divide
    ('\u2225', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ∥ parallel to
    ('\u2226', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ∦ not parallel to
    ('\u2241', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≁ not tilde
    ('\u2243', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≃ asymptotically equal to
    ('\u2244', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≄ not asymptotically equal to
    ('\u2245', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≅ approximately equal to
    ('\u2246', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≆ approximately but not actually equal to
    ('\u2247', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≇ neither approximately nor actually equal to
    ('\u224D', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≍ equivalent to
    ('\u2254', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≔ colon equals
    ('\u2257', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≗ ring equal to
    ('\u2259', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≙ estimates
    ('\u225A', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≚ equiangular to
    ('\u225B', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≛ star equals
    ('\u225C', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≜ delta equal to
    ('\u225F', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≟ questioned equal to
    ('\u2261', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≡ identical to
    ('\u2268', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≨ less-than but not equal to
    ('\u2269', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≩ greater-than but not equal to
    ('\u226A', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≪ much less-than
    ('\u226A\u0338', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≪̸ much less than with slash
    ('\u226B', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≫ much greater-than
    ('\u226B\u0338', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≫̸ much greater than with slash
    ('\u226D', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≭ not equivalent to
    ('\u2270', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≰ neither less-than nor equal to
    ('\u2271', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≱ neither greater-than nor equal to
    ('\u227A', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≺ precedes
    ('\u227B', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≻ succeeds
    ('\u227C', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≼ precedes or equal to
    ('\u227D', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ≽ succeeds or equal to
    ('\u2280', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⊀ does not precede
    ('\u2281', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⊁ does not succeed
    ('\u22A5', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⊥ up tack
    ('\u22B4', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⊴ normal subgroup of or equal to
    ('\u22B5', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⊵ contains as normal subgroup or equal to
    ('\u22C9', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ⋉ left normal factor semidirect product
    ('\u22CA', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ⋊ right normal factor semidirect product
    ('\u22CB', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ⋋ left semidirect product
    ('\u22CC', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ⋌ right semidirect product
    ('\u22D4', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋔ pitchfork
    ('\u22D6', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋖ less-than with dot
    ('\u22D7', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋗ greater-than with dot
    ('\u22D8', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋘ very much less-than
    ('\u22D9', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋙ very much greater-than
    ('\u22EA', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋪ not normal subgroup of
    ('\u22EB', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋫ does not contain as normal subgroup
    ('\u22EC', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋬ not normal subgroup of or equal to
    ('\u22ED', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⋭ does not contain as normal subgroup or equal
    ('\u25A0', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ■ black square
    ('\u25A1', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # □ white square
    ('\u25AA', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▪ black small square
    ('\u25AB', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▫ white small square
    ('\u25AD', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▭ white rectangle
    ('\u25AE', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▮ black vertical rectangle
    ('\u25AF', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▯ white vertical rectangle
    ('\u25B0', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▰ black parallelogram
    ('\u25B1', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ▱ white parallelogram
    ('\u25B3', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # △ white up-pointing triangle
    ('\u25B4', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▴ black up-pointing small triangle
    ('\u25B5', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▵ white up-pointing small triangle
    ('\u25B6', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▶ black right-pointing triangle
    ('\u25B7', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▷ white right-pointing triangle
    ('\u25B8', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▸ black right-pointing small triangle
    ('\u25B9', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▹ white right-pointing small triangle
    ('\u25BC', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▼ black down-pointing triangle
    ('\u25BD', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▽ white down-pointing triangle
    ('\u25BE', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▾ black down-pointing small triangle
    ('\u25BF', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ▿ white down-pointing small triangle
    ('\u25C0', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◀ black left-pointing triangle
    ('\u25C1', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◁ white left-pointing triangle
    ('\u25C2', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◂ black left-pointing small triangle
    ('\u25C3', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◃ white left-pointing small triangle
    ('\u25C4', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◄ black left-pointing pointer
    ('\u25C5', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◅ white left-pointing pointer
    ('\u25C6', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◆ black diamond
    ('\u25C7', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◇ white diamond
    ('\u25C8', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◈ white diamond containing black small diamond
    ('\u25C9', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◉ fisheye
    ('\u25CC', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◌ dotted circle
    ('\u25CD', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◍ circle with vertical fill
    ('\u25CE', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◎ bullseye
    ('\u25CF', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ● black circle
    ('\u25D6', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◖ left half black circle
    ('\u25D7', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◗ right half black circle
    ('\u25E6', 'infix'): {'priority': 260, 'lspace': 4, 'rspace': 4, }, # ◦ white bullet
    ('\u29C0', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⧀ circled less-than
    ('\u29C1', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⧁ circled greater-than
    ('\u29E3', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⧣ equals sign and slanted parallel
    ('\u29E4', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⧤ equals sign and slanted parallel with tilde above
    ('\u29E5', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⧥ identical to and slanted parallel
    ('\u29E6', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⧦ gleich stark
    ('\u29F3', 'infix'): {'priority': 260, 'lspace': 3, 'rspace': 3, }, # ⧳ error-barred black circle
    ('\u2A87', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⪇ less-than and single-line not equal to
    ('\u2A88', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⪈ greater-than and single-line not equal to
    ('\u2AAF', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⪯ precedes above single-line equals sign
    ('\u2AAF\u0338', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⪯̸ precedes above single-line equals sign with slash
    ('\u2AB0', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⪰ succeeds above single-line equals sign
    ('\u2AB0\u0338', 'infix'): {'priority': 260, 'lspace': 5, 'rspace': 5, }, # ⪰̸ succeeds above single-line equals sign with slash
    ('\u2044', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, 'stretchy': True, }, # ⁄ fraction slash
    ('\u2206', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ∆ increment
    ('\u220A', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∊ small element of
    ('\u220D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∍ small contains as member
    ('\u220E', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ∎ end of proof
    ('\u2215', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, 'stretchy': True, }, # ∕ division slash
    ('\u2217', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ∗ asterisk operator
    ('\u2218', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ∘ ring operator
    ('\u2219', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ∙ bullet operator
    ('\u221F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∟ right angle
    ('\u2223', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∣ divides
    ('\u2236', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∶ ratio
    ('\u2237', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∷ proportion
    ('\u2238', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ∸ dot minus
    ('\u2239', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∹ excess
    ('\u223A', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ∺ geometric proportion
    ('\u223B', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∻ homothetic
    ('\u223D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∽ reversed tilde
    ('\u223D\u0331', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ∽̱ reversed tilde with underline
    ('\u223E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ∾ inverted lazy s
    ('\u223F', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ∿ sine wave
    ('\u2242', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≂ minus tilde
    ('\u2242\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≂̸ minus tilde with slash
    ('\u224A', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≊ almost equal or equal to
    ('\u224B', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≋ triple tilde
    ('\u224C', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≌ all equal to
    ('\u224E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≎ geometrically equivalent to
    ('\u224E\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≎̸ geometrically equivalent to with slash
    ('\u224F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≏ difference between
    ('\u224F\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≏̸ difference between with slash
    ('\u2250', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≐ approaches the limit
    ('\u2251', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≑ geometrically equal to
    ('\u2252', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≒ approximately equal to or the image of
    ('\u2253', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≓ image of or approximately equal to
    ('\u2255', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≕ equals colon
    ('\u2256', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≖ ring in equal to
    ('\u2258', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≘ corresponds to
    ('\u225D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≝ equal to by definition
    ('\u225E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≞ measured by
    ('\u2263', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≣ strictly equivalent to
    ('\u2266', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≦ less-than over equal to
    ('\u2266\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≦̸ less-than over equal to with slash
    ('\u2267', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≧ greater-than over equal to
    ('\u226C', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≬ between
    ('\u2272', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≲ less-than or equivalent to
    ('\u2273', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≳ greater-than or equivalent to
    ('\u2274', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≴ neither less-than nor equivalent to
    ('\u2275', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≵ neither greater-than nor equivalent to
    ('\u2276', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≶ less-than or greater-than
    ('\u2277', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≷ greater-than or less-than
    ('\u2278', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≸ neither less-than nor greater-than
    ('\u2279', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≹ neither greater-than nor less-than
    ('\u227E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≾ precedes or equivalent to
    ('\u227F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≿ succeeds or equivalent to
    ('\u227F\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ≿̸ succeeds or equivalent to with slash
    ('\u228C', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊌ multiset
    ('\u228D', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊍ multiset multiplication
    ('\u228E', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊎ multiset union
    ('\u228F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊏ square image of
    ('\u228F\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊏̸ square image of with slash
    ('\u2290', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊐ square original of
    ('\u2290\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊐̸ square original of with slash
    ('\u2291', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊑ square image of or equal to
    ('\u2292', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊒ square original of or equal to
    ('\u2293', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊓ square cap
    ('\u2294', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊔ square cup
    ('\u229A', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊚ circled ring operator
    ('\u229B', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊛ circled asterisk operator
    ('\u229C', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊜ circled equals
    ('\u229D', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊝ circled dash
    ('\u22A6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊦ assertion
    ('\u22A7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊧ models
    ('\u22AA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊪ triple vertical bar right turnstile
    ('\u22AB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊫ double vertical bar double right turnstile
    ('\u22B0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊰ precedes under relation
    ('\u22B1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊱ succeeds under relation
    ('\u22B2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊲ normal subgroup of
    ('\u22B3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊳ contains as normal subgroup
    ('\u22B6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊶ original of
    ('\u22B7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊷ image of
    ('\u22B9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⊹ hermitian conjugate matrix
    ('\u22BA', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊺ intercalate
    ('\u22BB', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊻ xor
    ('\u22BC', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊼ nand
    ('\u22BD', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⊽ nor
    ('\u22BE', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⊾ right angle with arc
    ('\u22BF', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⊿ right triangle
    ('\u22C4', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋄ diamond operator
    ('\u22C6', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋆ star operator
    ('\u22C7', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋇ division times
    ('\u22C8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋈ bowtie
    ('\u22CD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋍ reversed tilde equals
    ('\u22CE', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋎ curly logical or
    ('\u22CF', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋏ curly logical and
    ('\u22D0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋐ double subset
    ('\u22D1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋑ double superset
    ('\u22D2', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋒ double intersection
    ('\u22D3', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⋓ double union
    ('\u22D5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋕ equal and parallel to
    ('\u22DA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋚ less-than equal to or greater-than
    ('\u22DB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋛ greater-than equal to or less-than
    ('\u22DC', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋜ equal to or less-than
    ('\u22DD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋝ equal to or greater-than
    ('\u22DE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋞ equal to or precedes
    ('\u22DF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋟ equal to or succeeds
    ('\u22E0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋠ does not precede or equal
    ('\u22E1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋡ does not succeed or equal
    ('\u22E2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋢ not square image of or equal to
    ('\u22E3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋣ not square original of or equal to
    ('\u22E4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋤ square image of or not equal to
    ('\u22E5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋥ square original of or not equal to
    ('\u22E6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋦ less-than but not equivalent to
    ('\u22E7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋧ greater-than but not equivalent to
    ('\u22E8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋨ precedes but not equivalent to
    ('\u22E9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋩ succeeds but not equivalent to
    ('\u22F0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋰ up right diagonal ellipsis
    ('\u22F2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋲ element of with long horizontal stroke
    ('\u22F3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋳ element of with vertical bar at end of horizontal stroke
    ('\u22F4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋴ small element of with vertical bar at end of horizontal stroke
    ('\u22F5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋵ element of with dot above
    ('\u22F6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋶ element of with overbar
    ('\u22F7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋷ small element of with overbar
    ('\u22F8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋸ element of with underbar
    ('\u22F9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋹ element of with two horizontal strokes
    ('\u22FA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋺ contains with long horizontal stroke
    ('\u22FB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋻ contains with vertical bar at end of horizontal stroke
    ('\u22FC', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋼ small contains with vertical bar at end of horizontal stroke
    ('\u22FD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋽ contains with overbar
    ('\u22FE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋾ small contains with overbar
    ('\u22FF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⋿ z notation bag membership
    ('\u25B2', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ▲ black up-pointing triangle
    ('\u2758', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ❘ light vertical bar
    ('\u2981', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦁ z notation spot
    ('\u2982', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦂ z notation type colon
    ('\u29A0', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦠ spherical angle opening left
    ('\u29A1', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦡ spherical angle opening up
    ('\u29A2', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦢ turned angle
    ('\u29A3', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦣ reversed angle
    ('\u29A4', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦤ angle with underbar
    ('\u29A5', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦥ reversed angle with underbar
    ('\u29A6', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦦ oblique angle opening up
    ('\u29A7', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦧ oblique angle opening down
    ('\u29A8', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦨ measured angle with open arm ending in arrow pointing up and right
    ('\u29A9', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦩ measured angle with open arm ending in arrow pointing up and left
    ('\u29AA', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦪ measured angle with open arm ending in arrow pointing down and right
    ('\u29AB', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦫ measured angle with open arm ending in arrow pointing down and left
    ('\u29AC', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦬ measured angle with open arm ending in arrow pointing right and up
    ('\u29AD', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦭ measured angle with open arm ending in arrow pointing left and up
    ('\u29AE', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦮ measured angle with open arm ending in arrow pointing right and down
    ('\u29AF', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦯ measured angle with open arm ending in arrow pointing left and down
    ('\u29B0', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦰ reversed empty set
    ('\u29B1', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦱ empty set with overbar
    ('\u29B2', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦲ empty set with small circle above
    ('\u29B3', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦳ empty set with right arrow above
    ('\u29B4', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦴ empty set with left arrow above
    ('\u29B5', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⦵ circle with horizontal bar
    ('\u29B6', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦶ circled vertical bar
    ('\u29B7', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦷ circled parallel
    ('\u29B8', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦸ circled reverse solidus
    ('\u29B9', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦹ circled perpendicular
    ('\u29BA', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦺ circle divided by horizontal bar and top half divided by vertical bar
    ('\u29BB', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦻ circle with superimposed x
    ('\u29BC', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦼ circled anticlockwise-rotated division sign
    ('\u29BD', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦽ up arrow through circle
    ('\u29BE', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦾ circled white bullet
    ('\u29BF', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⦿ circled bullet
    ('\u29C2', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧂ circle with small circle to the right
    ('\u29C3', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧃ circle with two horizontal strokes to the right
    ('\u29C4', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧄ squared rising diagonal slash
    ('\u29C5', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧅ squared falling diagonal slash
    ('\u29C6', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧆ squared asterisk
    ('\u29C7', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧇ squared small circle
    ('\u29C8', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧈ squared square
    ('\u29C9', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧉ two joined squares
    ('\u29CA', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧊ triangle with dot above
    ('\u29CB', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧋ triangle with underbar
    ('\u29CC', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧌ s in triangle
    ('\u29CD', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧍ triangle with serifs at bottom
    ('\u29CE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧎ right triangle above left triangle
    ('\u29CF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧏ left triangle beside vertical bar
    ('\u29CF\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧏̸ left triangle beside vertical bar with slash
    ('\u29D0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧐ vertical bar beside right triangle
    ('\u29D0\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧐̸ vertical bar beside right triangle with slash
    ('\u29D1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧑ bowtie with left half black
    ('\u29D2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧒ bowtie with right half black
    ('\u29D3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧓ black bowtie
    ('\u29D4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧔ times with left half black
    ('\u29D5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧕ times with right half black
    ('\u29D6', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧖ white hourglass
    ('\u29D7', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧗ black hourglass
    ('\u29D8', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧘ left wiggly fence
    ('\u29D9', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧙ right wiggly fence
    ('\u29DB', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧛ right double wiggly fence
    ('\u29DC', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧜ incomplete infinity
    ('\u29DD', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧝ tie over infinity
    ('\u29DE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧞ infinity negated with vertical bar
    ('\u29E0', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧠ square with contoured outline
    ('\u29E1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⧡ increases as
    ('\u29E2', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧢ shuffle product
    ('\u29E7', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧧ thermodynamic
    ('\u29E8', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧨ down-pointing triangle with left half black
    ('\u29E9', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧩ down-pointing triangle with right half black
    ('\u29EA', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧪ black diamond with down arrow
    ('\u29EB', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧫ black lozenge
    ('\u29EC', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧬ white circle with down arrow
    ('\u29ED', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧭ black circle with down arrow
    ('\u29EE', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧮ error-barred white square
    ('\u29F0', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧰ error-barred white diamond
    ('\u29F1', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧱ error-barred black diamond
    ('\u29F2', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧲ error-barred white circle
    ('\u29F5', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧵ reverse solidus operator
    ('\u29F6', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧶ solidus with overbar
    ('\u29F7', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧷ reverse solidus with horizontal stroke
    ('\u29F8', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧸ big solidus
    ('\u29F9', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧹ big reverse solidus
    ('\u29FA', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧺ double plus
    ('\u29FB', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⧻ triple plus
    ('\u29FE', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧾ tiny
    ('\u29FF', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⧿ miny
    ('\u2A1D', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⨝ join
    ('\u2A1E', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⨞ large left triangle operator
    ('\u2A1F', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⨟ z notation schema composition
    ('\u2A20', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⨠ z notation schema piping
    ('\u2A21', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⨡ z notation schema projection
    ('\u2A22', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨢ plus sign with small circle above
    ('\u2A23', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨣ plus sign with circumflex accent above
    ('\u2A24', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨤ plus sign with tilde above
    ('\u2A25', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨥ plus sign with dot below
    ('\u2A26', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨦ plus sign with tilde below
    ('\u2A27', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨧ plus sign with subscript two
    ('\u2A28', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨨ plus sign with black triangle
    ('\u2A29', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨩ minus sign with comma above
    ('\u2A2A', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨪ minus sign with dot below
    ('\u2A2B', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨫ minus sign with falling dots
    ('\u2A2C', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨬ minus sign with rising dots
    ('\u2A2D', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨭ plus sign in left half circle
    ('\u2A2E', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨮ plus sign in right half circle
    ('\u2A30', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨰ multiplication sign with dot above
    ('\u2A31', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨱ multiplication sign with underbar
    ('\u2A32', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨲ semidirect product with bottom closed
    ('\u2A33', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨳ smash product
    ('\u2A34', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨴ multiplication sign in left half circle
    ('\u2A35', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨵ multiplication sign in right half circle
    ('\u2A36', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨶ circled multiplication sign with circumflex accent
    ('\u2A37', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨷ multiplication sign in double circle
    ('\u2A38', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨸ circled division sign
    ('\u2A39', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨹ plus sign in triangle
    ('\u2A3A', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨺ minus sign in triangle
    ('\u2A3B', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨻ multiplication sign in triangle
    ('\u2A3C', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨼ interior product
    ('\u2A3D', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨽ righthand interior product
    ('\u2A3E', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⨾ z notation relational composition
    ('\u2A40', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩀ intersection with dot
    ('\u2A41', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩁ union with minus sign
    ('\u2A42', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩂ union with overbar
    ('\u2A43', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩃ intersection with overbar
    ('\u2A44', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩄ intersection with logical and
    ('\u2A45', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩅ union with logical or
    ('\u2A46', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩆ union above intersection
    ('\u2A47', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩇ intersection above union
    ('\u2A48', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩈ union above bar above intersection
    ('\u2A49', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩉ intersection above bar above union
    ('\u2A4A', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩊ union beside and joined with union
    ('\u2A4B', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩋ intersection beside and joined with intersection
    ('\u2A4C', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩌ closed union with serifs
    ('\u2A4D', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩍ closed intersection with serifs
    ('\u2A4E', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩎ double square intersection
    ('\u2A4F', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩏ double square union
    ('\u2A50', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩐ closed union with serifs and smash product
    ('\u2A51', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩑ logical and with dot above
    ('\u2A52', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩒ logical or with dot above
    ('\u2A53', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩓ double logical and
    ('\u2A54', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩔ double logical or
    ('\u2A55', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩕ two intersecting logical and
    ('\u2A56', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩖ two intersecting logical or
    ('\u2A57', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩗ sloping large or
    ('\u2A58', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩘ sloping large and
    ('\u2A59', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩙ logical or overlapping logical and
    ('\u2A5A', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩚ logical and with middle stem
    ('\u2A5B', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩛ logical or with middle stem
    ('\u2A5C', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩜ logical and with horizontal dash
    ('\u2A5D', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩝ logical or with horizontal dash
    ('\u2A5E', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩞ logical and with double overbar
    ('\u2A5F', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩟ logical and with underbar
    ('\u2A60', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩠ logical and with double underbar
    ('\u2A61', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩡ small vee with underbar
    ('\u2A62', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩢ logical or with double overbar
    ('\u2A63', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩣ logical or with double underbar
    ('\u2A64', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩤ z notation domain antirestriction
    ('\u2A65', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩥ z notation range antirestriction
    ('\u2A66', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩦ equals sign with dot below
    ('\u2A67', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩧ identical with dot above
    ('\u2A68', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩨ triple horizontal bar with double vertical stroke
    ('\u2A69', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩩ triple horizontal bar with triple vertical stroke
    ('\u2A6A', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩪ tilde operator with dot above
    ('\u2A6B', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩫ tilde operator with rising dots
    ('\u2A6C', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩬ similar minus similar
    ('\u2A6D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩭ congruent with dot above
    ('\u2A6E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩮ equals with asterisk
    ('\u2A6F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩯ almost equal to with circumflex accent
    ('\u2A70', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩰ approximately equal or equal to
    ('\u2A71', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩱ equals sign above plus sign
    ('\u2A72', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⩲ plus sign above equals sign
    ('\u2A73', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩳ equals sign above tilde operator
    ('\u2A74', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩴ double colon equal
    ('\u2A75', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩵ two consecutive equals signs
    ('\u2A76', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩶ three consecutive equals signs
    ('\u2A77', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩷ equals sign with two dots above and two dots below
    ('\u2A78', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩸ equivalent with four dots above
    ('\u2A79', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩹ less-than with circle inside
    ('\u2A7A', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩺ greater-than with circle inside
    ('\u2A7B', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩻ less-than with question mark above
    ('\u2A7C', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩼ greater-than with question mark above
    ('\u2A7D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩽ less-than or slanted equal to
    ('\u2A7D\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩽̸ less-than or slanted equal to with slash
    ('\u2A7E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩾ greater-than or slanted equal to
    ('\u2A7E\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩾̸ greater-than or slanted equal to with slash
    ('\u2A7F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⩿ less-than or slanted equal to with dot inside
    ('\u2A80', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪀ greater-than or slanted equal to with dot inside
    ('\u2A81', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪁ less-than or slanted equal to with dot above
    ('\u2A82', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪂ greater-than or slanted equal to with dot above
    ('\u2A83', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪃ less-than or slanted equal to with dot above right
    ('\u2A84', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪄ greater-than or slanted equal to with dot above left
    ('\u2A85', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪅ less-than or approximate
    ('\u2A86', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪆ greater-than or approximate
    ('\u2A89', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪉ less-than and not approximate
    ('\u2A8A', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪊ greater-than and not approximate
    ('\u2A8B', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪋ less-than above double-line equal above greater-than
    ('\u2A8C', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪌ greater-than above double-line equal above less-than
    ('\u2A8D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪍ less-than above similar or equal
    ('\u2A8E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪎ greater-than above similar or equal
    ('\u2A8F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪏ less-than above similar above greater-than
    ('\u2A90', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪐ greater-than above similar above less-than
    ('\u2A91', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪑ less-than above greater-than above double-line equal
    ('\u2A92', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪒ greater-than above less-than above double-line equal
    ('\u2A93', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪓ less-than above slanted equal above greater-than above slanted equal
    ('\u2A94', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪔ greater-than above slanted equal above less-than above slanted equal
    ('\u2A95', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪕ slanted equal to or less-than
    ('\u2A96', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪖ slanted equal to or greater-than
    ('\u2A97', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪗ slanted equal to or less-than with dot inside
    ('\u2A98', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪘ slanted equal to or greater-than with dot inside
    ('\u2A99', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪙ double-line equal to or less-than
    ('\u2A9A', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪚ double-line equal to or greater-than
    ('\u2A9B', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪛ double-line slanted equal to or less-than
    ('\u2A9C', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪜ double-line slanted equal to or greater-than
    ('\u2A9D', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪝ similar or less-than
    ('\u2A9E', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪞ similar or greater-than
    ('\u2A9F', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪟ similar above less-than above equals sign
    ('\u2AA0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪠ similar above greater-than above equals sign
    ('\u2AA1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪡ double nested less-than
    ('\u2AA1\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪡̸ double nested less-than with slash
    ('\u2AA2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪢ double nested greater-than
    ('\u2AA2\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪢̸ double nested greater-than with slash
    ('\u2AA3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪣ double nested less-than with underbar
    ('\u2AA4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪤ greater-than overlapping less-than
    ('\u2AA5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪥ greater-than beside less-than
    ('\u2AA6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪦ less-than closed by curve
    ('\u2AA7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪧ greater-than closed by curve
    ('\u2AA8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪨ less-than closed by curve above slanted equal
    ('\u2AA9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪩ greater-than closed by curve above slanted equal
    ('\u2AAA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪪ smaller than
    ('\u2AAB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪫ larger than
    ('\u2AAC', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪬ smaller than or equal to
    ('\u2AAD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪭ larger than or equal to
    ('\u2AAE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪮ equals sign with bumpy above
    ('\u2AB1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪱ precedes above single-line not equal to
    ('\u2AB2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪲ succeeds above single-line not equal to
    ('\u2AB3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪳ precedes above equals sign
    ('\u2AB4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪴ succeeds above equals sign
    ('\u2AB5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪵ precedes above not equal to
    ('\u2AB6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪶ succeeds above not equal to
    ('\u2AB7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪷ precedes above almost equal to
    ('\u2AB8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪸ succeeds above almost equal to
    ('\u2AB9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪹ precedes above not almost equal to
    ('\u2ABA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪺ succeeds above not almost equal to
    ('\u2ABB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪻ double precedes
    ('\u2ABC', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪼ double succeeds
    ('\u2ABD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪽ subset with dot
    ('\u2ABE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪾ superset with dot
    ('\u2ABF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⪿ subset with plus sign below
    ('\u2AC0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫀ superset with plus sign below
    ('\u2AC1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫁ subset with multiplication sign below
    ('\u2AC2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫂ superset with multiplication sign below
    ('\u2AC3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫃ subset of or equal to with dot above
    ('\u2AC4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫄ superset of or equal to with dot above
    ('\u2AC5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫅ subset of above equals sign
    ('\u2AC6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫆ superset of above equals sign
    ('\u2AC7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫇ subset of above tilde operator
    ('\u2AC8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫈ superset of above tilde operator
    ('\u2AC9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫉ subset of above almost equal to
    ('\u2ACA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫊ superset of above almost equal to
    ('\u2ACB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫋ subset of above not equal to
    ('\u2ACC', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫌ superset of above not equal to
    ('\u2ACD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫍ square left open box operator
    ('\u2ACE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫎ square right open box operator
    ('\u2ACF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫏ closed subset
    ('\u2AD0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫐ closed superset
    ('\u2AD1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫑ closed subset or equal to
    ('\u2AD2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫒ closed superset or equal to
    ('\u2AD3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫓ subset above superset
    ('\u2AD4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫔ superset above subset
    ('\u2AD5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫕ subset above subset
    ('\u2AD6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫖ superset above superset
    ('\u2AD7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫗ superset beside subset
    ('\u2AD8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫘ superset beside and joined by dash with subset
    ('\u2AD9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫙ element of opening downwards
    ('\u2ADA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫚ pitchfork with tee top
    ('\u2ADB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫛ transversal intersection
    ('\u2ADD', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫝ nonforking
    ('\u2ADD\u0338', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫝̸ nonforking with slash
    ('\u2ADE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫞ short left tack
    ('\u2ADF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫟ short down tack
    ('\u2AE0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫠ short up tack
    ('\u2AE1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫡ perpendicular with s
    ('\u2AE2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫢ vertical bar triple right turnstile
    ('\u2AE3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫣ double vertical bar left turnstile
    ('\u2AE4', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫤ vertical bar double left turnstile
    ('\u2AE5', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫥ double vertical bar double left turnstile
    ('\u2AE6', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫦ long dash from left member of double vertical
    ('\u2AE7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫧ short down tack with overbar
    ('\u2AE8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫨ short up tack with underbar
    ('\u2AE9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫩ short up tack above short down tack
    ('\u2AEA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫪ double down tack
    ('\u2AEB', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫫ double up tack
    ('\u2AEC', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫬ double stroke not sign
    ('\u2AED', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫭ reversed double stroke not sign
    ('\u2AEE', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫮ does not divide with reversed negation slash
    ('\u2AEF', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫯ vertical line with circle above
    ('\u2AF0', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫰ vertical line with circle below
    ('\u2AF1', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫱ down tack with circle below
    ('\u2AF2', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫲ parallel with horizontal stroke
    ('\u2AF3', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫳ parallel with tilde operator
    ('\u2AF4', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⫴ triple vertical bar binary relation
    ('\u2AF5', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⫵ triple vertical bar with horizontal stroke
    ('\u2AF6', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⫶ triple colon operator
    ('\u2AF7', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫷ triple nested less-than
    ('\u2AF8', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫸ triple nested greater-than
    ('\u2AF9', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫹ double-line slanted less-than or equal to
    ('\u2AFA', 'infix'): {'priority': 265, 'lspace': 5, 'rspace': 5, }, # ⫺ double-line slanted greater-than or equal to
    ('\u2AFB', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⫻ triple solidus binary relation
    ('\u2AFD', 'infix'): {'priority': 265, 'lspace': 4, 'rspace': 4, }, # ⫽ double solidus operator
    ('\u2AFE', 'infix'): {'priority': 265, 'lspace': 3, 'rspace': 3, }, # ⫾ white vertical bar
    ('|', 'infix'): {'priority': 270, 'lspace': 2, 'rspace': 2, 'fence': True, 'stretchy': True, 'symmetric': True, }, # | vertical line
    ('||', 'infix'): {'priority': 270, 'lspace': 2, 'rspace': 2, 'fence': True, 'stretchy': True, 'symmetric': True, }, # || multiple character operator: ||
    ('|||', 'infix'): {'priority': 270, 'lspace': 2, 'rspace': 2, 'fence': True, 'stretchy': True, 'symmetric': True, }, # ||| multiple character operator: |||
    ('\u2190', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ← leftwards arrow
    ('\u2191', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↑ upwards arrow
    ('\u2192', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # → rightwards arrow
    ('\u2193', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↓ downwards arrow
    ('\u2194', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↔ left right arrow
    ('\u2195', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↕ up down arrow
    ('\u2196', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↖ north west arrow
    ('\u2197', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↗ north east arrow
    ('\u2198', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↘ south east arrow
    ('\u2199', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↙ south west arrow
    ('\u219A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ↚ leftwards arrow with stroke
    ('\u219B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ↛ rightwards arrow with stroke
    ('\u219C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↜ leftwards wave arrow
    ('\u219D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↝ rightwards wave arrow
    ('\u219E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↞ leftwards two headed arrow
    ('\u219F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↟ upwards two headed arrow
    ('\u21A0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↠ rightwards two headed arrow
    ('\u21A1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↡ downwards two headed arrow
    ('\u21A2', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↢ leftwards arrow with tail
    ('\u21A3', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↣ rightwards arrow with tail
    ('\u21A4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↤ leftwards arrow from bar
    ('\u21A5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↥ upwards arrow from bar
    ('\u21A6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↦ rightwards arrow from bar
    ('\u21A7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↧ downwards arrow from bar
    ('\u21A8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↨ up down arrow with base
    ('\u21A9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↩ leftwards arrow with hook
    ('\u21AA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↪ rightwards arrow with hook
    ('\u21AB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↫ leftwards arrow with loop
    ('\u21AC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↬ rightwards arrow with loop
    ('\u21AD', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↭ left right wave arrow
    ('\u21AE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ↮ left right arrow with stroke
    ('\u21AF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↯ downwards zigzag arrow
    ('\u21B0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↰ upwards arrow with tip leftwards
    ('\u21B1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↱ upwards arrow with tip rightwards
    ('\u21B2', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↲ downwards arrow with tip leftwards
    ('\u21B3', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↳ downwards arrow with tip rightwards
    ('\u21B4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↴ rightwards arrow with corner downwards
    ('\u21B5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↵ downwards arrow with corner leftwards
    ('\u21B6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ↶ anticlockwise top semicircle arrow
    ('\u21B7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ↷ clockwise top semicircle arrow
    ('\u21B8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ↸ north west arrow to long bar
    ('\u21B9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↹ leftwards arrow to bar over rightwards arrow to bar
    ('\u21BA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ↺ anticlockwise open circle arrow
    ('\u21BB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ↻ clockwise open circle arrow
    ('\u21BC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↼ leftwards harpoon with barb upwards
    ('\u21BD', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ↽ leftwards harpoon with barb downwards
    ('\u21BE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↾ upwards harpoon with barb rightwards
    ('\u21BF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ↿ upwards harpoon with barb leftwards
    ('\u21C0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇀ rightwards harpoon with barb upwards
    ('\u21C1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇁ rightwards harpoon with barb downwards
    ('\u21C2', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇂ downwards harpoon with barb rightwards
    ('\u21C3', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇃ downwards harpoon with barb leftwards
    ('\u21C4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇄ rightwards arrow over leftwards arrow
    ('\u21C5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇅ upwards arrow leftwards of downwards arrow
    ('\u21C6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇆ leftwards arrow over rightwards arrow
    ('\u21C7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇇ leftwards paired arrows
    ('\u21C8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇈ upwards paired arrows
    ('\u21C9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇉ rightwards paired arrows
    ('\u21CA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇊ downwards paired arrows
    ('\u21CB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇋ leftwards harpoon over rightwards harpoon
    ('\u21CC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇌ rightwards harpoon over leftwards harpoon
    ('\u21CD', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇍ leftwards double arrow with stroke
    ('\u21CE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇎ left right double arrow with stroke
    ('\u21CF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇏ rightwards double arrow with stroke
    ('\u21D0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇐ leftwards double arrow
    ('\u21D1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇑ upwards double arrow
    ('\u21D2', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇒ rightwards double arrow
    ('\u21D3', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇓ downwards double arrow
    ('\u21D4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇔ left right double arrow
    ('\u21D5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇕ up down double arrow
    ('\u21D6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇖ north west double arrow
    ('\u21D7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇗ north east double arrow
    ('\u21D8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇘ south east double arrow
    ('\u21D9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇙ south west double arrow
    ('\u21DA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇚ leftwards triple arrow
    ('\u21DB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇛ rightwards triple arrow
    ('\u21DC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇜ leftwards squiggle arrow
    ('\u21DD', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇝ rightwards squiggle arrow
    ('\u21DE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⇞ upwards arrow with double stroke
    ('\u21DF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⇟ downwards arrow with double stroke
    ('\u21E0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇠ leftwards dashed arrow
    ('\u21E1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇡ upwards dashed arrow
    ('\u21E2', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇢ rightwards dashed arrow
    ('\u21E3', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇣ downwards dashed arrow
    ('\u21E4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇤ leftwards arrow to bar
    ('\u21E5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇥ rightwards arrow to bar
    ('\u21E6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇦ leftwards white arrow
    ('\u21E7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇧ upwards white arrow
    ('\u21E8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇨ rightwards white arrow
    ('\u21E9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇩ downwards white arrow
    ('\u21EA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇪ upwards white arrow from bar
    ('\u21EB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇫ upwards white arrow on pedestal
    ('\u21EC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇬ upwards white arrow on pedestal with horizontal bar
    ('\u21ED', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇭ upwards white arrow on pedestal with vertical bar
    ('\u21EE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇮ upwards white double arrow
    ('\u21EF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇯ upwards white double arrow on pedestal
    ('\u21F0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇰ rightwards white arrow from wall
    ('\u21F1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⇱ north west arrow to corner
    ('\u21F2', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⇲ south east arrow to corner
    ('\u21F3', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇳ up down white arrow
    ('\u21F4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇴ right arrow with small circle
    ('\u21F5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⇵ downwards arrow leftwards of upwards arrow
    ('\u21F6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇶ three rightwards arrows
    ('\u21F7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇷ leftwards arrow with vertical stroke
    ('\u21F8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇸ rightwards arrow with vertical stroke
    ('\u21F9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇹ left right arrow with vertical stroke
    ('\u21FA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇺ leftwards arrow with double vertical stroke
    ('\u21FB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇻ rightwards arrow with double vertical stroke
    ('\u21FC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⇼ left right arrow with double vertical stroke
    ('\u21FD', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇽ leftwards open-headed arrow
    ('\u21FE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇾ rightwards open-headed arrow
    ('\u21FF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⇿ left right open-headed arrow
    ('\u22B8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⊸ multimap
    ('\u27F0', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⟰ upwards quadruple arrow
    ('\u27F1', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⟱ downwards quadruple arrow
    ('\u27F5', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟵ long leftwards arrow
    ('\u27F6', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟶ long rightwards arrow
    ('\u27F7', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟷ long left right arrow
    ('\u27F8', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟸ long leftwards double arrow
    ('\u27F9', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟹ long rightwards double arrow
    ('\u27FA', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟺ long left right double arrow
    ('\u27FB', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟻ long leftwards arrow from bar
    ('\u27FC', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟼ long rightwards arrow from bar
    ('\u27FD', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟽ long leftwards double arrow from bar
    ('\u27FE', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟾ long rightwards double arrow from bar
    ('\u27FF', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⟿ long rightwards squiggle arrow
    ('\u2900', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤀ rightwards two-headed arrow with vertical stroke
    ('\u2901', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤁ rightwards two-headed arrow with double vertical stroke
    ('\u2902', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤂ leftwards double arrow with vertical stroke
    ('\u2903', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤃ rightwards double arrow with vertical stroke
    ('\u2904', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤄ left right double arrow with vertical stroke
    ('\u2905', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤅ rightwards two-headed arrow from bar
    ('\u2906', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤆ leftwards double arrow from bar
    ('\u2907', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤇ rightwards double arrow from bar
    ('\u2908', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤈ downwards arrow with horizontal stroke
    ('\u2909', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤉ upwards arrow with horizontal stroke
    ('\u290A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⤊ upwards triple arrow
    ('\u290B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⤋ downwards triple arrow
    ('\u290C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⤌ leftwards double dash arrow
    ('\u290D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⤍ rightwards double dash arrow
    ('\u290E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⤎ leftwards triple dash arrow
    ('\u290F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⤏ rightwards triple dash arrow
    ('\u2910', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⤐ rightwards two-headed triple dash arrow
    ('\u2911', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤑ rightwards arrow with dotted stem
    ('\u2912', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⤒ upwards arrow to bar
    ('\u2913', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⤓ downwards arrow to bar
    ('\u2914', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤔ rightwards arrow with tail with vertical stroke
    ('\u2915', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤕ rightwards arrow with tail with double vertical stroke
    ('\u2916', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤖ rightwards two-headed arrow with tail
    ('\u2917', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤗ rightwards two-headed arrow with tail with vertical stroke
    ('\u2918', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤘ rightwards two-headed arrow with tail with double vertical stroke
    ('\u2919', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤙ leftwards arrow-tail
    ('\u291A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤚ rightwards arrow-tail
    ('\u291B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤛ leftwards double arrow-tail
    ('\u291C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤜ rightwards double arrow-tail
    ('\u291D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤝ leftwards arrow to black diamond
    ('\u291E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤞ rightwards arrow to black diamond
    ('\u291F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤟ leftwards arrow from bar to black diamond
    ('\u2920', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤠ rightwards arrow from bar to black diamond
    ('\u2921', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⤡ north west and south east arrow
    ('\u2922', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⤢ north east and south west arrow
    ('\u2923', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤣ north west arrow with hook
    ('\u2924', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤤ north east arrow with hook
    ('\u2925', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤥ south east arrow with hook
    ('\u2926', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤦ south west arrow with hook
    ('\u2927', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤧ north west arrow and north east arrow
    ('\u2928', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤨ north east arrow and south east arrow
    ('\u2929', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤩ south east arrow and south west arrow
    ('\u292A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤪ south west arrow and north west arrow
    ('\u292B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤫ rising diagonal crossing falling diagonal
    ('\u292C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤬ falling diagonal crossing rising diagonal
    ('\u292D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤭ south east arrow crossing north east arrow
    ('\u292E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤮ north east arrow crossing south east arrow
    ('\u292F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤯ falling diagonal crossing north east arrow
    ('\u2930', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤰ rising diagonal crossing south east arrow
    ('\u2931', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤱ north east arrow crossing north west arrow
    ('\u2932', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤲ north west arrow crossing north east arrow
    ('\u2933', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤳ wave arrow pointing directly right
    ('\u2934', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤴ arrow pointing rightwards then curving upwards
    ('\u2935', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤵ arrow pointing rightwards then curving downwards
    ('\u2936', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤶ arrow pointing downwards then curving leftwards
    ('\u2937', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤷ arrow pointing downwards then curving rightwards
    ('\u2938', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤸ right-side arc clockwise arrow
    ('\u2939', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤹ left-side arc anticlockwise arrow
    ('\u293A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤺ top arc anticlockwise arrow
    ('\u293B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤻ bottom arc anticlockwise arrow
    ('\u293C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤼ top arc clockwise arrow with minus
    ('\u293D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⤽ top arc anticlockwise arrow with plus
    ('\u293E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤾ lower right semicircular clockwise arrow
    ('\u293F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⤿ lower left semicircular anticlockwise arrow
    ('\u2940', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥀ anticlockwise closed circle arrow
    ('\u2941', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥁ clockwise closed circle arrow
    ('\u2942', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥂ rightwards arrow above short leftwards arrow
    ('\u2943', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥃ leftwards arrow above short rightwards arrow
    ('\u2944', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥄ short rightwards arrow above leftwards arrow
    ('\u2945', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥅ rightwards arrow with plus below
    ('\u2946', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥆ leftwards arrow with plus below
    ('\u2947', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥇ rightwards arrow through x
    ('\u2948', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥈ left right arrow through small circle
    ('\u2949', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥉ upwards two-headed arrow from small circle
    ('\u294A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥊ left barb up right barb down harpoon
    ('\u294B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥋ left barb down right barb up harpoon
    ('\u294C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥌ up barb right down barb left harpoon
    ('\u294D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥍ up barb left down barb right harpoon
    ('\u294E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥎ left barb up right barb up harpoon
    ('\u294F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥏ up barb right down barb right harpoon
    ('\u2950', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥐ left barb down right barb down harpoon
    ('\u2951', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥑ up barb left down barb left harpoon
    ('\u2952', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥒ leftwards harpoon with barb up to bar
    ('\u2953', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥓ rightwards harpoon with barb up to bar
    ('\u2954', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥔ upwards harpoon with barb right to bar
    ('\u2955', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥕ downwards harpoon with barb right to bar
    ('\u2956', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥖ leftwards harpoon with barb down to bar
    ('\u2957', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥗ rightwards harpoon with barb down to bar
    ('\u2958', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥘ upwards harpoon with barb left to bar
    ('\u2959', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥙ downwards harpoon with barb left to bar
    ('\u295A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥚ leftwards harpoon with barb up from bar
    ('\u295B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥛ rightwards harpoon with barb up from bar
    ('\u295C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥜ upwards harpoon with barb right from bar
    ('\u295D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥝ downwards harpoon with barb right from bar
    ('\u295E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥞ leftwards harpoon with barb down from bar
    ('\u295F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, 'accent': True, }, # ⥟ rightwards harpoon with barb down from bar
    ('\u2960', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥠ upwards harpoon with barb left from bar
    ('\u2961', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥡ downwards harpoon with barb left from bar
    ('\u2962', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥢ leftwards harpoon with barb up above leftwards harpoon with barb down
    ('\u2963', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥣ upwards harpoon with barb left beside upwards harpoon with barb right
    ('\u2964', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥤ rightwards harpoon with barb up above rightwards harpoon with barb down
    ('\u2965', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥥ downwards harpoon with barb left beside downwards harpoon with barb right
    ('\u2966', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥦ leftwards harpoon with barb up above rightwards harpoon with barb up
    ('\u2967', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥧ leftwards harpoon with barb down above rightwards harpoon with barb down
    ('\u2968', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥨ rightwards harpoon with barb up above leftwards harpoon with barb up
    ('\u2969', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥩ rightwards harpoon with barb down above leftwards harpoon with barb down
    ('\u296A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥪ leftwards harpoon with barb up above long dash
    ('\u296B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥫ leftwards harpoon with barb down below long dash
    ('\u296C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥬ rightwards harpoon with barb up above long dash
    ('\u296D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥭ rightwards harpoon with barb down below long dash
    ('\u296E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥮ upwards harpoon with barb left beside downwards harpoon with barb right
    ('\u296F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⥯ downwards harpoon with barb left beside upwards harpoon with barb right
    ('\u2970', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥰ right double arrow with rounded head
    ('\u2971', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥱ equals sign above rightwards arrow
    ('\u2972', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥲ tilde operator above rightwards arrow
    ('\u2973', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥳ leftwards arrow above tilde operator
    ('\u2974', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥴ rightwards arrow above tilde operator
    ('\u2975', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥵ rightwards arrow above almost equal to
    ('\u2976', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥶ less-than above leftwards arrow
    ('\u2977', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥷ leftwards arrow through less-than
    ('\u2978', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥸ greater-than above rightwards arrow
    ('\u2979', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥹ subset above rightwards arrow
    ('\u297A', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥺ leftwards arrow through subset
    ('\u297B', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥻ superset above leftwards arrow
    ('\u297C', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥼ left fish tail
    ('\u297D', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'accent': True, }, # ⥽ right fish tail
    ('\u297E', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥾ up fish tail
    ('\u297F', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⥿ down fish tail
    ('\u2999', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦙ dotted fence
    ('\u299A', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦚ vertical zigzag line
    ('\u299B', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦛ measured angle opening left
    ('\u299C', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦜ right angle variant with square
    ('\u299D', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦝ measured right angle with dot
    ('\u299E', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦞ angle with s inside
    ('\u299F', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⦟ acute angle
    ('\u29DF', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⧟ double-ended multimap
    ('\u29EF', 'infix'): {'priority': 270, 'lspace': 3, 'rspace': 3, }, # ⧯ error-barred black square
    ('\u29F4', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, }, # ⧴ rule-delayed
    ('\u2B45', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⭅ leftwards quadruple arrow
    ('\u2B46', 'infix'): {'priority': 270, 'lspace': 5, 'rspace': 5, 'stretchy': True, }, # ⭆ rightwards quadruple arrow
    ('+', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # + plus sign
    ('+', 'prefix'): {'priority': 275, 'lspace': 0, 'rspace': 1, }, # + plus sign
    ('-', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # - hyphen-minus
    ('-', 'prefix'): {'priority': 275, 'lspace': 0, 'rspace': 1, }, # - hyphen-minus
    ('\u00B1', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # ± plus-minus sign
    ('\u00B1', 'prefix'): {'priority': 275, 'lspace': 0, 'rspace': 1, }, # ± plus-minus sign
    ('\u2212', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # − minus sign
    ('\u2212', 'prefix'): {'priority': 275, 'lspace': 0, 'rspace': 1, }, # − minus sign
    ('\u2213', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # ∓ minus-or-plus sign
    ('\u2213', 'prefix'): {'priority': 275, 'lspace': 0, 'rspace': 1, }, # ∓ minus-or-plus sign
    ('\u2214', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # ∔ dot plus
    ('\u229E', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # ⊞ squared plus
    ('\u229F', 'infix'): {'priority': 275, 'lspace': 4, 'rspace': 4, }, # ⊟ squared minus
    ('\u2211', 'prefix'): {'priority': 290, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ∑ n-ary summation
    ('\u2A0A', 'prefix'): {'priority': 290, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨊ modulo two sum
    ('\u2A0B', 'prefix'): {'priority': 290, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨋ summation with integral
    ('\u222C', 'prefix'): {'priority': 300, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∬ double integral
    ('\u222D', 'prefix'): {'priority': 300, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∭ triple integral
    ('\u2295', 'infix'): {'priority': 300, 'lspace': 4, 'rspace': 4, }, # ⊕ circled plus
    ('\u2296', 'infix'): {'priority': 300, 'lspace': 4, 'rspace': 4, }, # ⊖ circled minus
    ('\u2298', 'infix'): {'priority': 300, 'lspace': 4, 'rspace': 4, }, # ⊘ circled division slash
    ('\u2A01', 'prefix'): {'priority': 300, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨁ n-ary circled plus operator
    ('\u222B', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∫ integral
    ('\u222E', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∮ contour integral
    ('\u222F', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∯ surface integral
    ('\u2230', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∰ volume integral
    ('\u2231', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∱ clockwise integral
    ('\u2232', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∲ clockwise contour integral
    ('\u2233', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ∳ anticlockwise contour integral
    ('\u2A0C', 'prefix'): {'priority': 310, 'lspace': 0, 'rspace': 1, 'largeop': True, 'symmetric': True, }, # ⨌ quadruple integral operator
    ('\u2A0D', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨍ finite part integral
    ('\u2A0E', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨎ integral with double stroke
    ('\u2A0F', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨏ integral average with slash
    ('\u2A10', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨐ circulation function
    ('\u2A11', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨑ anticlockwise integration
    ('\u2A12', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨒ line integration with rectangular path around pole
    ('\u2A13', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨓ line integration with semicircular path around pole
    ('\u2A14', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨔ line integration not including the pole
    ('\u2A15', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨕ integral around a point operator
    ('\u2A16', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨖ quaternion integral operator
    ('\u2A17', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨗ integral with leftwards arrow with hook
    ('\u2A18', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨘ integral with times sign
    ('\u2A19', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨙ integral with intersection
    ('\u2A1A', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨚ integral with union
    ('\u2A1B', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨛ integral with overbar
    ('\u2A1C', 'prefix'): {'priority': 310, 'lspace': 1, 'rspace': 2, 'largeop': True, 'symmetric': True, }, # ⨜ integral with underbar
    ('\u22C3', 'prefix'): {'priority': 320, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⋃ n-ary union
    ('\u2A03', 'prefix'): {'priority': 320, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨃ n-ary union operator with dot
    ('\u2A04', 'prefix'): {'priority': 320, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨄ n-ary union operator with plus
    ('\u22C0', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⋀ n-ary logical and
    ('\u22C1', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⋁ n-ary logical or
    ('\u22C2', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⋂ n-ary intersection
    ('\u2A00', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨀ n-ary circled dot operator
    ('\u2A02', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨂ n-ary circled times operator
    ('\u2A05', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨅ n-ary square intersection operator
    ('\u2A06', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨆ n-ary square union operator
    ('\u2A07', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨇ two logical and operator
    ('\u2A08', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨈ two logical or operator
    ('\u2A09', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⨉ n-ary times operator
    ('\u2AFC', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⫼ large triple vertical bar operator
    ('\u2AFF', 'prefix'): {'priority': 330, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ⫿ n-ary white vertical bar
    ('\u2240', 'infix'): {'priority': 340, 'lspace': 4, 'rspace': 4, }, # ≀ wreath product
    ('\u220F', 'prefix'): {'priority': 350, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ∏ n-ary product
    ('\u2210', 'prefix'): {'priority': 350, 'lspace': 1, 'rspace': 2, 'largeop': True, 'movablelimits': True, 'symmetric': True, }, # ∐ n-ary coproduct
    ('\u2229', 'infix'): {'priority': 350, 'lspace': 4, 'rspace': 4, }, # ∩ intersection
    ('\u222A', 'infix'): {'priority': 350, 'lspace': 4, 'rspace': 4, }, # ∪ union
    ('*', 'infix'): {'priority': 390, 'lspace': 3, 'rspace': 3, }, # * asterisk
    ('.', 'infix'): {'priority': 390, 'lspace': 3, 'rspace': 3, }, # . full stop
    ('\u00D7', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # × multiplication sign
    ('\u2022', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # • bullet
    ('\u2043', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # ⁃ hyphen bullet
    ('\u2062', 'infix'): {'priority': 390, 'lspace': 0, 'rspace': 0, }, # ⁢ invisible times
    ('\u22A0', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # ⊠ squared times
    ('\u22A1', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # ⊡ squared dot operator
    ('\u22C5', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # ⋅ dot operator
    ('\u2A2F', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # ⨯ vector or cross product
    ('\u2A3F', 'infix'): {'priority': 390, 'lspace': 4, 'rspace': 4, }, # ⨿ amalgamation or coproduct
    ('\u00B7', 'infix'): {'priority': 400, 'lspace': 4, 'rspace': 4, }, # · middle dot
    ('\u2297', 'infix'): {'priority': 410, 'lspace': 4, 'rspace': 4, }, # ⊗ circled times
    ('%', 'infix'): {'priority': 640, 'lspace': 3, 'rspace': 3, }, # % percent sign
    ('\\', 'infix'): {'priority': 650, 'lspace': 0, 'rspace': 0, }, # \ reverse solidus
    ('\u2216', 'infix'): {'priority': 650, 'lspace': 4, 'rspace': 4, }, # ∖ set minus
    ('/', 'infix'): {'priority': 660, 'lspace': 1, 'rspace': 1, }, # / solidus
    ('\u00F7', 'infix'): {'priority': 660, 'lspace': 4, 'rspace': 4, }, # ÷ division sign
    ('\u2220', 'prefix'): {'priority': 670, 'lspace': 0, 'rspace': 0, }, # ∠ angle
    ('\u2221', 'prefix'): {'priority': 670, 'lspace': 0, 'rspace': 0, }, # ∡ measured angle
    ('\u2222', 'prefix'): {'priority': 670, 'lspace': 0, 'rspace': 0, }, # ∢ spherical angle
    ('\u00AC', 'prefix'): {'priority': 680, 'lspace': 2, 'rspace': 1, }, # ¬ not sign
    ('\u2299', 'infix'): {'priority': 710, 'lspace': 4, 'rspace': 4, }, # ⊙ circled dot operator
    ('\u2202', 'prefix'): {'priority': 740, 'lspace': 2, 'rspace': 1, }, # ∂ partial differential
    ('\u2207', 'prefix'): {'priority': 740, 'lspace': 2, 'rspace': 1, }, # ∇ nabla
    ('**', 'infix'): {'priority': 780, 'lspace': 1, 'rspace': 1, }, # ** multiple character operator: **
    ('<>', 'infix'): {'priority': 780, 'lspace': 1, 'rspace': 1, }, # <> multiple character operator: <>
    ('^', 'infix'): {'priority': 780, 'lspace': 1, 'rspace': 1, }, # ^ circumflex accent
    ('\u2032', 'postfix'): {'priority': 800, 'lspace': 0, 'rspace': 0, }, # ′ prime
    ('\u266D', 'postfix'): {'priority': 800, 'lspace': 0, 'rspace': 2, }, # ♭ music flat sign
    ('\u266E', 'postfix'): {'priority': 800, 'lspace': 0, 'rspace': 2, }, # ♮ music natural sign
    ('\u266F', 'postfix'): {'priority': 800, 'lspace': 0, 'rspace': 2, }, # ♯ music sharp sign
    ('!', 'postfix'): {'priority': 810, 'lspace': 1, 'rspace': 0, }, # ! exclamation mark
    ('!!', 'postfix'): {'priority': 810, 'lspace': 1, 'rspace': 0, }, # !! multiple character operator: !!
    ('//', 'infix'): {'priority': 820, 'lspace': 1, 'rspace': 1, }, # // multiple character operator: //
    ('@', 'infix'): {'priority': 825, 'lspace': 1, 'rspace': 1, }, # @ commercial at
    ('?', 'infix'): {'priority': 835, 'lspace': 1, 'rspace': 1, }, # ? question mark
    ('\u2145', 'prefix'): {'priority': 845, 'lspace': 2, 'rspace': 1, }, # ⅅ double-struck italic capital d
    ('\u2146', 'prefix'): {'priority': 845, 'lspace': 2, 'rspace': 0, }, # ⅆ double-struck italic small d
    ('\u221A', 'prefix'): {'priority': 845, 'lspace': 1, 'rspace': 1, 'stretchy': True, }, # √ square root
    ('\u221B', 'prefix'): {'priority': 845, 'lspace': 1, 'rspace': 1, }, # ∛ cube root
    ('\u221C', 'prefix'): {'priority': 845, 'lspace': 1, 'rspace': 1, }, # ∜ fourth root
    ('\u2061', 'infix'): {'priority': 850, 'lspace': 0, 'rspace': 0, }, # ⁡ function application
    ('"', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # " quotation mark
    ('&', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, }, # & ampersand
    ('\'', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ' apostrophe
    ('++', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, }, # ++ multiple character operator: ++
    ('--', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, }, # -- multiple character operator: --
    ('^', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ^ circumflex accent
    ('_', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # _ low line
    ('`', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ` grave accent
    ('~', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ~ tilde
    ('\u00A8', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ¨ diaeresis
    ('\u00AA', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ª feminine ordinal indicator
    ('\u00AF', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ¯ macron
    ('\u00B0', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, }, # ° degree sign
    ('\u00B2', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ² superscript two
    ('\u00B3', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ³ superscript three
    ('\u00B4', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ´ acute accent
    ('\u00B8', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ¸ cedilla
    ('\u00B9', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ¹ superscript one
    ('\u00BA', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # º masculine ordinal indicator
    ('\u02C6', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ˆ modifier letter circumflex accent
    ('\u02C7', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ˇ caron
    ('\u02C9', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ˉ modifier letter macron
    ('\u02CA', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ˊ modifier letter acute accent
    ('\u02CB', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ˋ modifier letter grave accent
    ('\u02CD', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ˍ modifier letter low macron
    ('\u02D8', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ˘ breve
    ('\u02D9', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ˙ dot above
    ('\u02DA', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ˚ ring above
    ('\u02DC', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ˜ small tilde
    ('\u02DD', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ˝ double acute accent
    ('\u02F7', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ˷ modifier letter low tilde
    ('\u0302', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, #  combining circumflex accent
    ('\u0311', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, #  combining inverted breve
    ('\u201A', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‚ single low-9 quotation mark
    ('\u201B', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‛ single high-reversed-9 quotation mark
    ('\u201E', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # „ double low-9 quotation mark
    ('\u201F', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‟ double high-reversed-9 quotation mark
    ('\u2033', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ″ double prime
    ('\u2034', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‴ triple prime
    ('\u2035', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‵ reversed prime
    ('\u2036', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‶ reversed double prime
    ('\u2037', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ‷ reversed triple prime
    ('\u203E', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ‾ overline
    ('\u2057', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, # ⁗ quadruple prime
    ('\u2064', 'infix'): {'priority': 880, 'lspace': 0, 'rspace': 0, }, # ⁤ invisible plus
    ('\u20DB', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, #  combining three dots above
    ('\u20DC', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'accent': True, }, #  combining four dots above
    ('\u23B4', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⎴ top square bracket
    ('\u23B5', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⎵ bottom square bracket
    ('\u23DC', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⏜ top parenthesis
    ('\u23DD', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⏝ bottom parenthesis
    ('\u23DE', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⏞ top curly bracket
    ('\u23DF', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⏟ bottom curly bracket
    ('\u23E0', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⏠ top tortoise shell bracket
    ('\u23E1', 'postfix'): {'priority': 880, 'lspace': 0, 'rspace': 0, 'stretchy': True, 'accent': True, }, # ⏡ bottom tortoise shell bracket
    ('_', 'infix'): {'priority': 900, 'lspace': 1, 'rspace': 1, }, # _ low line
}
