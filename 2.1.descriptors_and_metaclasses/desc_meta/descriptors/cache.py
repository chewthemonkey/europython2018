class Cache(object):
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, instance, owner):
        import time
        print('doing expensive calculation at first access')
        time.sleep(1)
        value = 42
        instance.__dict__[self.attr_name] = value
        return value

class WithCache(object):
    attr = Cache('attr')
