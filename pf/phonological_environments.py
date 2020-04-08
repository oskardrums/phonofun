from .sound import *
def get_sounds_dict(wordlst:list):
    sounds_dict = {}
    for word in wordlst:
        for sound in word:
            if sound not in sounds_dict.values():
                sounds_dict[sound]=[]
    return sounds_dict

