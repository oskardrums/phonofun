from .features import FEATURES,NON_DIACRITIC_TO_FEATURES
from .ipa import *
class Sound(object):
    def __init__(self, content: str, type_: str= None, features: dict=None):
            self.content = content
            self.features = self.translate_features()
            self.type_ = type_
						
    def __repr__(self, singular=False):
        output = self.content + " "
        if singular:
            for feature in self.features.values():
                output += feature + " "
        return output[:-1]

    def __eq__(self, other):
        return self.content == other.content

    def compare(self, other):
        #returns all common features for 2 sounds
        if self == other:
            return self.features.values()
        commons = []
        if self.type_ != other.type_:
            commons.append("TYPES")
        for feature in self.features.values():
            if self.features[feature] == other.features[feature]:
                commons.append(feature)
        return commons

    def get_diffs(self, other):
        #returns all different features for 2 sounds
        if self == other:
            return []
        diffs = []
        if self.type_ != other.type_:
            return ["TYPES"]
        for feature in self.features.values():
            if self.features[feature] != other.features[feature]:
                diffs.append(feature)
        return diffs

    def getfeature(self,feature):
        return self.features[feature]

    def translate_features(self):# TODO update to with diacritics
        features =NON_DIACRITIC_TO_FEATURES[self.content]
        features_dict = {}
        for num,feature in enumerate(FEATURES):
            features_dict[feature] = features[num]
        return features_dict

    def determine_type(self):
        if self.content in VOWELS:
            self.type_ = "VOWEL"
        else:
            self.type_ = "CONSONANT"
