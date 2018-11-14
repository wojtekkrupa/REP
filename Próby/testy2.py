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

class Mojaklasa:
    zmienna = "blah"
    def funkcja(self):
        print("To jest wiadomosc wewnatrz klasy.")

mojobiekt = Mojaklasa()

#mojobiekt.zmienna = "ple"

print(mojobiekt.zmienna)
print(mojobiekt.funkcja())


decorated_print = decorator(print)
decorated_print(hello)

sum