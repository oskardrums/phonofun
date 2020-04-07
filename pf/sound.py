from .features import FEATURES
class Sound(object):
    def __init__(self, content: str, type_: str, features: dict):
            self.content = content
            self.features = self.translate_features(features)
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
        if self == other:
            return []
        if self.type_ != other.type_:
            return ["TYPE"]
        diffs = []
        for feature in self.features.values():
            if self.features[feature] != other.features[feature]:
                diffs.append(feature)
        return diffs

    def getfeature(self,feature):
        return self.features[feature]
    def translate_features(self,features):
        return features # TODO figure out
    
