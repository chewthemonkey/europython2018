class WrongReadOnly(object):

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        return 42

class Wrong(object):
    attr_wrong_ro = WrongReadOnly('attr_wrong_ro')
    def __init__(self, attr):
        attr_wrong_ro = attr


class RightReadOnly(object):

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        return 42

    def __set__(self, instance, value):
        raise AttributeError('attribute "{}" is read-only'.format(self.attr_name))

class Right(object):
    attr_ro = RightReadOnly('attr_ro')

    def __init__(self, attr):
        attr_ro = attr
