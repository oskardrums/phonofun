import pf

def test_ipa():
    for group in [pf.DIACRITICS, pf.STRESS, pf.TONES, pf.VOWELS, pf.TIES]:
        for literal in group:
            assert len(literal) <= 1, f"{literal} is too long"

def test():
    test_ipa()
    s = pf.PhonologicalSound()
    print(pf.DIACRITICS, pf.STRESS, pf.TONES, pf.VOWELS, pf.TIES)

if __name__ == "__main__":
    test()
