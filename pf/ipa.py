DIACRITICS = "ː ̆ ʰ ʲ ʷ ̚ ̃ ̈ ̩ ̯ ̥ ̬ ̪ ̺ ̝ ̞ ̟ ̠  ˑ ˤ ˀ ᵊ ʱ ˡ ⁿ ʳ ᵗ ˠ ʼ  ̹  ̜   ̤   ̰   ̼  ̘  ̙  ̻   ̴   ˞   ̊   ̽".split(' ')
STRESS     = "ˈ ˌ".split(' ')
TONES      = "̀ ̄ ́ ̂ ̌ ᷈".split(' ')
TIES       = "͡ ͜".split(' ')
PREFIXES = STRESS
SUFFIXES = TONES + DIACRITICS
INFIXES  = TIES
VOWELS = "ɑ æ ɐ ə ɚ ɵ ɘ ɛ ɜ ɝ ɪ ɨ ɔ œ ɒ ø ʊ ʉ ʌ ʏ ɤ ɯ a e i o u".split(' ')
CONTANTS = "β ɓ ç ɕ ð ɖ ɗ ɠ ɢ ħ ɦ ɥ ɧ ʜ ʝ ɟ ɫ ɭ ɬ ʟ ɮ ɱ ŋ ɲ ɳ ɴ ɸ ɾ ɹ ʁ ʀ ɻ ɽ ʃ ʂ θ ʈ ʋ ʍ χ ɣ ʎ ʒ ʐ ʑ ʔ ʕ b c d f g h i j k l m n p q r s t v w x z".split(' ')
BASES = VOWELS + CONTANTS

def tokenize(word):
    """
    Breaks a `str` containting the IPA phonetic representation of a word to a 
    `list` of `str`s, each representing a single phonetic sound
    """
    token = ""
    tokens = []

    for i, s in enumerate(word):
        if token:
            if s in PREFIXES:
                if token[-1] not in PREFIXES:
                    raise ValueError
                token += s
            elif s in BASES:
                if token[-1] in PREFIXES + INFIXES:
                    token += s
                elif token[-1] in BASES + SUFFIXES:
                    tokens.append(token)
                    token = s
                else:
                    raise ValueError
            elif s in INFIXES:
                if token[-1] not in BASES:
                    raise ValueError
                token += s
            elif s in SUFFIXES:
                if token[-1] not in BASES + SUFFIXES:
                    raise ValueError
                token += s
            else:
                raise ValueError
        else:
            if s not in PREFIXES + BASES:
                raise ValueError
            token = s
    tokens.append(token)

    return tokens
