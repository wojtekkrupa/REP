#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bb
#
# Created:     09-11-2018
# Copyright:   (c) bb 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z = {**x, **y}
print(z)
m = {**x}
n = {**y}
print(m)
print(n)

a = [1,2,3]
b = a
print(a)
print(b)
print(a == b)
print(a is b)
c = list(a)
print(c)
print(a == c)
print(a is c)

names = [
    'alice',
    'bob',
    'wojtek',
    'anna',
    ]
# po anna jest przecinek
print(names)