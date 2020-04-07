from . import sound

def literal_constrains(literal):
    return set()


class PhonologicalSound(object):

    def __init__(self, constraints=None):
        self.constraints = constraints or set()

    @classmethod
    def from_literal(cls, literal):
        return cls(constraints=literal_constrains(literal))


