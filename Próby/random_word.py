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
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

print(randomword(10))