from .ipa import TONES, TIES, STRESS


FEATURES = (
    'CONS',
    'SON',
    'SYLL',
    'LABIAL',
    'ROUND',
    'CORONAL',
    'ANT',
    'DIST',
    'DORSAL',
    'HIGH',
    'LOW',
    'BACK',
    'TENSE',
    'PHARYNGIAL',
    'ATR',
    'VOICE',
    'SG',
    'CG',
    'CONT',
    'STRIDENT',
    'LATERAL',
    'DELREL',
    'NASAL',
)


# CONS SON SYLL LABIAL ROUND CORONAL ANT DIST DORSAL HIGH LOW BACK TENSE PHARYNGIAL ATR VOICE SG CG CONT STRIDENT LATERAL DELREL NASAL
NON_DIACRITIC_TO_FEATURES = {
    't':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '-', '-', '-', '-', '-',],
    'd':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '-', '-', '-', '-', '-',],
    's':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+', '+', '-', '-', '-',],
    'z':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '+', '-', '-', '-',],
    'ɬ':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '-', '+', '-', '+', '-', '+', '-', '-',],
    'ɮ':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '+', '-', '-',],
    'θ':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+', '-', '-', '-', '-',],
    'ð':  ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ʃ':  ['+', '-', '-', '-', '0', '+', '-', '+', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+', '-', '-', '-', '-',],
    'ʒ':  ['+', '-', '-', '-', '0', '+', '-', '+', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'c':  ['+', '-', '-', '-', '0', '+', '-', '+', '+', '+', '-', '-', '-', '-', '0', '-', '-', '-', '-', '-', '-', '-', '-',],
    'ɟ':  ['+', '-', '-', '-', '0', '+', '-', '+', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '-',],
    'ç':  ['+', '-', '-', '-', '0', '+', '-', '+', '+', '+', '-', '-', '-', '-', '0', '-', '-', '-', '+', '-', '-', '-', '-',],
    'ʝ':  ['+', '-', '-', '-', '0', '+', '-', '+', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'p':  ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '-', '-', '-', '-', '-',],
    'b':  ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '-', '-', '-', '-', '-',],
    'f':  ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+', '+', '-', '-', '-',],
    'v':  ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '+', '-', '-', '-',],
    'ɸ':  ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+', '-', '-', '-', '-',],
    'β':  ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'k':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '-', '-', '-', '-', '-', '-', '-', '-',],
    'g':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '-',],
    'x':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '-', '-', '-', '+', '-', '-', '-', '-',],
    'ɣ':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'q':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '-', '-', '+', '-', '-', '0', '-', '-', '-', '-', '-', '-', '-', '-',],
    'ɢ':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '-', '-', '+', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '-',],
    'χ':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '-', '-', '+', '-', '-', '0', '-', '-', '-', '+', '-', '-', '-', '-',],
    'ʁ':  ['+', '-', '-', '-', '0', '-', '0', '0', '+', '-', '-', '+', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ħ':  ['+', '-', '-', '-', '0', '-', '0', '0', '-', '0', '0', '0', '0', '+', '-', '-', '-', '-', '+', '-', '-', '-', '-',],
    'ʕ':  ['+', '-', '-', '-', '0', '-', '0', '0', '-', '0', '0', '0', '0', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'h':  ['-', '-', '-', '-', '0', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '-', '+', '-', '+', '-', '-', '-', '-',],
    'ɦ':  ['-', '-', '-', '-', '0', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '+', '+', '-', '+', '-', '-', '-', '-',],
    'ʔ':  ['-', '-', '-', '-', '0', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '-', '-', '+', '-', '-', '-', '-', '-',],
    't͡ʃ': ['+', '-', '-', '-', '0', '+', '-', '+', '+', '+', '-', '-', '-', '-', '0', '-', '-', '-', '+-', '+', '-', '+', '-',],
    'd͡ʒ': ['+', '-', '-', '-', '0', '+', '-', '+', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '+-', '+', '-', '+', '-',],
    't͡s': ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+-', '+', '-', '+', '-',],
    'd͡z': ['+', '-', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+-', '+', '-', '+', '-',],
    'k͡x': ['+', '-', '-', '-', '0', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '-', '-', '-', '+-', '-', '-', '+', '-',],
    'p͡f': ['+', '-', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '-', '-', '-', '+-', '+', '-', '+', '-',],
    'm':  ['+', '+', '-', '+', '-', '-', '0', '0', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '-', '-', '-', '-', '+',],
    'n':  ['+', '+', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '-', '-', '-', '-', '+',],
    'ŋ':  ['+', '+', '-', '-', '0', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '+',],
    'ɳ':  ['+', '+', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '+',],
    'ɲ':  ['+', '+', '-', '-', '0', '-', '0', '0', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '+',],
    'ɴ':  ['+', '+', '-', '-', '0', '-', '0', '0', '+', '-', '-', '+', '-', '-', '0', '+', '-', '-', '-', '-', '-', '-', '+',],
    'l':  ['+', '+', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '+', '-', '-',],
    'ɫ':  ['+', '+', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '+', '-', '+', '-', '-', '+', '-', '+', '-', '-',],
    'ʎ':  ['+', '+', '-', '-', '0', '-', '0', '0', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '+', '-', '+', '-', '-',],
    'r':  ['+', '+', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɹ':  ['+', '+', '-', '-', '0', '+', '+', '-', '-', '0', '0', '0', '0', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ʀ':  ['+', '+', '-', '-', '0', '-', '0', '0', '+', '-', '-', '+', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'j':  ['-', '+', '-', '+', '-', '-', '0', '0', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'w':  ['-', '+', '-', '+', '+', '-', '0', '0', '+', '+', '-', '+', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɥ':  ['-', '+', '-', '+', '+', '-', '0', '0', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɰ':  ['-', '+', '-', '+', '+', '-', '0', '0', '+', '+', '-', '-', '-', '-', '0', '+', '-', '-', '+', '-', '-', '-', '-',],

    'i':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '+', '-', '-', '+', '+', '+', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɪ':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '+', '-', '-', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'u':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '+', '-', '+', '+', '+', '+', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ʊ':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '+', '-', '+', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'e':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '-', '-', '-', '+', '+', '+', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɛ':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '-', '-', '-', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'o':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '-', '-', '+', '+', '+', '+', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɔ':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '-', '-', '+', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'a':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '-', '+', '-', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'æ':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '-', '+', '-', '+', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'y':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '+', '-', '-', '+', '+', '+', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ʏ':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '+', '-', '-', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ø':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '-', '-', '-', '+', '+', '+', '+', '-', '-', '+', '-', '-', '-', '-',],
    'œ':  ['-', '+', '+', '+', '-', '-', '0', '0', '+', '-', '-', '-', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ə':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '-', '-', '+', '-', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],
    'ɯ':  ['-', '+', '+', '+', '+', '-', '0', '0', '+', '+', '-', '+', '+', '+', '-', '+', '-', '-', '+', '-', '-', '-', '-',],

    # TODO: ɱ, ɾ, ɻ, ɽ, ʍ and some others
}

DIACRITIC_TO_FEATURES = {
    '̥':  {'VOICE': '-'},
    '̬':  {'VOICE': '+'},
    'ʰ': {'ASPIRATED': '+'},
    '̹':  {'ROUND': '+'},
    '̜':  {'ROUND': '-'},
    '̟':  {}, # TODO, advanced
    '̠':  {}, # TODO, retracted
    '̪':  {'DENTAL': '+'},
    '̺':  {'APICAL': '+'},
    '̈':  {}, # TODO, centralized
    '̩':  {'SYLL': '+'},
    '̯':  {'SYLL': '-'},
    '˞':  {'RHOTICITY': '+'},
    '̤':  {'VOICE': 'b'},
    '̰':  {'VOICE': 'c'},
    'ʷ': {'ROUND': '+'},
    'ʲ': {'PALATAL': '+'},
    'ˤ': {'PHARYNGIAL': '+'},
    '̃':  {'NASAL': '+'},
    'ˡ': {'RELEASE': 'l'},
    'ⁿ': {'RELEASE': 'n'},
    '̚':  {'RELEASE': '-'},
    '̘':  {'ATR': '+'},
    '̙':  {'ATR': '-'},
    '̝':  {}, # TODO: raised
    '̞':  {}, # TODO: lowered
    'ː': {'LENGTH': 'l'},
    'ˑ': {'LENGTH': 'h'},
    '̆':  {'LENGTH': 's'},
}


def _handle_non_diacritic(mapping):
    assert len(mapping) == len(FEATURES)
    return {FEATURES[i]: mapping[i] for i in range(len(FEATURES))}


def _fix_literal(literal):
    for t in TIES:
        literal = literal.replace(t, '͡')

    for s in STRESS:
        literal = literal.replace(s, '')

    return literal


def _handle_affricates(literal):
    features = {}

    if 't͡ʃ' in literal:
        features = _handle_non_diacritic(NON_DIACRITIC_TO_FEATURES.get('t͡ʃ'))
        literal = literal.replace('t͡ʃ', '', 1)
    elif 'd͡ʒ' in literal:
        features = _handle_non_diacritic(NON_DIACRITIC_TO_FEATURES.get('d͡ʒ'))
        literal = literal.replace('d͡ʒ', '', 1)
    elif 't͡s' in literal:
        features = _handle_non_diacritic(NON_DIACRITIC_TO_FEATURES.get('t͡s'))
        literal = literal.replace('t͡s', '', 1)
    elif 'd͡z' in literal:
        features = _handle_non_diacritic(NON_DIACRITIC_TO_FEATURES.get('d͡z'))
        literal = literal.replace('d͡z', '', 1)
    elif 'k͡x' in literal:
        features = _handle_non_diacritic(NON_DIACRITIC_TO_FEATURES.get('k͡x'))
        literal = literal.replace('k͡x', '', 1)
    elif 'p͡f' in literal:
        features = _handle_non_diacritic(NON_DIACRITIC_TO_FEATURES.get('p͡f'))
        literal = literal.replace('p͡f', '', 1)

    # there should be no more ties
    if '͡' in literal:
        raise NotImplementedError('non-standard affricate in literal {}'.format(literal))

    return literal, features


def parse_literal(literal):
    """
    parses a literal string into a `dict` of phonological features.
    for most of the features, the values could be either '+', '-' or '0' (for NA).
    some of the features have different values, like 'RELEASE' which has
    'l' (lateral release), 'n' (nasal release) and '-' (no audible release).
    """
    literal = _fix_literal(literal)
    literal, features = _handle_affricates(literal)

    # next, handle everything else
    for c in literal:
        current = NON_DIACRITIC_TO_FEATURES.get(c)
        if current is not None:
            features.update(_handle_non_diacritic(current))
            continue

        if c in TONES:
            features['TONE'] = '+'
            continue

        current = DIACRITIC_TO_FEATURES.get(c)
        if current is not None:
            features.update(current)
            continue

        raise NotImplementedError('unsupported character "{}" in literal {}'.format(c, literal))

    return features
