

from functools import partial

class Protector(object):

    def __init__(self, cls, meth):
        self.cls = cls
        self.meth = meth

    def __get__(self, instance, owner):
        return partial(self.meth, self)

    def __set__(self, instance, value):
        raise AttributeError('cannot set method')


def protect_methods(cls):
    for name, obj in cls.__dict__.items():
        if callable(obj):
            setattr(cls, name, Protector(cls, obj))
    return cls


@protect_methods
class Protected(object):

    def meth1(self):
        print('called')
        return 42

    def meth2(self):
        print('called')
        return 142

if __name__ == '__main__':
    p = Protected()
    print(p.meth1())
    p.meth1 = 43
