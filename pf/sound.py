class Sound(object):
    def __init__(self, content: str, type_: str, features: list):
            self.content = content
            self.features = features
            self.type = type_
						
    def __repr__(self, singular=False):
        output = self.content + " "
        if singular:
            for feature in self.features:
                output += feature + " "
        return output[:-1]

    def __eq__(self, other):
        return self.content == other.content

    def compare(self, other):
        if self == other:
            return True
        for feature in self.features: # TODO: understand tomer's feature structure
            return False
