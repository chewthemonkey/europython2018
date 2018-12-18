
class Unprotected(object):

    def meth(self):
        print('called')
        return 42


if __name__ == '__main__':
    u = Unprotected()
    print(u.meth())
    u.meth = 43
    print(u.meth)
