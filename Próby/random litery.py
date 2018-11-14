#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      www
#
# Created:     13-11-2018
# Copyright:   (c) www 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random
def random_id(length):
    #number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    id = ''
    for i in range(0,length,2):
        #id += random.choice(number)
        id += random.choice(alpha)
    return id
x = random_id(20)
print(x)