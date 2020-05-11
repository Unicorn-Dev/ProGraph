class ToLongName(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, it is too long '.format(self.value)


class VretexAlreadyExist(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, is already exist'.format(self.value)

class VretexDoesNotExist(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, one of '\
            'vertex isn\'t exist'.format(self.value)

class EdgeDoesNotExist(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, '\
            'edge isn\'t exist'.format(self.value)

class VretexNumberError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, '\
            'expected 2 vertex'.format(self.value)

class IncorrectWeightError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, '\
            'weight should be integer'.format(self.value)
