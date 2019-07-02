import math
#import sys
from sys import *
print("Hello World")
class User(object):
    pass


if __name__ == '__main__':
    print(dir(User()))
print(math.pi)
#print(sys.version)
print(version)
print(executable)

class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()