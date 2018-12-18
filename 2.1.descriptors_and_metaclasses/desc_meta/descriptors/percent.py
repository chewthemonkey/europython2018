class Percent(object):

    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __set__(self, instance, value):
        if not 0 <= value <= 100:
            msg ='Value must be between 0 and 100. Got: {}.'.format(value)
            raise ValueError(msg)
        instance.__dict__[self.attr_name] = value


class WithPercent(object):
    percent = Percent('percent')

    def __init__(self, percent):
        self.percent = percent
