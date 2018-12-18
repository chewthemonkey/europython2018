
class Special(object):
    def __contains__(self, item):
        print('got', item)
        return True

if __name__ == '__main__':
    s = Special()
    print('abc' in s)
    s.__contains__ = 43
    print('abc' in s)
