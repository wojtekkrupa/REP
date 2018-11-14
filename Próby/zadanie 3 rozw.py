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

def append_to_file(file_name, lines):
    """
    Funkcja dodająca linijkę do pliku o podanej nazwie
    (string, list)
    :param file_name:
    :param lines:
    :return:
    """
    with open(file_name, 'a+') as f:
        lines = [line if line[-1]=='\n' else line+'\n' for line in lines ]
        f.writelines(lines)

with open('dane_osobowe.csv', 'r') as plik_zrodlowy:
    linie = plik_zrodlowy.readlines()
    print(linie)
    for l in linie:
        kod_pocztowy = l.split(',')[7]
        if kod_pocztowy[0] == "2":
            append_to_file('dane_lubelskie.csv', [l])
        else:
            print("Podano nieprawidłowy kod pocztowy.")