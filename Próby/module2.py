#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bb
#
# Created:     12-11-2018
# Copyright:   (c) bb 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

squares = {1:1,2:4,3:"error",4:16}
squares[8] = 64
squares[3] = 9
print(squares)

primes = {1:2,2:3,4:7,7:17}
print(primes[primes[4]])