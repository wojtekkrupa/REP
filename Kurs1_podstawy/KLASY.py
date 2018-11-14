#-------------------------------------------------------------------------------
# Name:        klasy
# Purpose:
#
# Author:      www
#
# Created:     07-11-2018
# Copyright:   (c) www 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Zwierz:
    # poniżej definicja klasy
    # 1 opis klasy
    '''pierwsza klasa'''
    # definiujemy metodę klasy czyli funkcję wewnątrz klasy

    #rodzaj          # definiujemy atrybuty ktorych warotci beda wspolne dla wszytskich obiektow klas
    rodzaj = "zwierzę"             # w tym celu wpisujemy nazwę atrybutu wewnątrz defnicji klasy pomijając "self"
    def __init__(self, gatunek, wiek):    #po self podajemy argumenty ktore będziemy podawawac przy tworzeniu instancji klas
        self.gatunek = gatunek                              #podczas inicjalizacji klasy stawiamy atrybuty
        self.wiek = wiek
                        # self wskazuje że atrybut będzie przypisany do konkretnej instancji klasy(obiektu)
    def podaj_gatunek(self):    #podaj_gatunek to nazwa metody
        # definicja funkcji) tu funcja 'wypisuje' jeden gatunek
        print('lis')


# tworzymy obiekt typu Zwierz czyli instancję naszej klasy
# wywołujemy klasę jak funkcję
#a = Zwierz()
# tworzymy drugi obiekt
#b = Zwierz()
#print(a)
#print(b)
# wywołujemy metodę podaj_gatunek, bez podania argumentu z zewnąrz bo self
#wskazuje bieżący obiekt np. 'a' czy 'b' klasy
# a - nazwa zmiennej obiektu
#a.podaj_gatunek()
#b.podaj_gatunek()
a = Zwierz('lis', 5)    #teraz potrzebne wartosci argumentu gatunek oraz wiek
b = Zwierz('pyton', 2)
#wyswietkamy wartosci atrybutow
print(a.gatunek, a.wiek)
print(b.gatunek, b.wiek)
# i otrzymamy rożne wartosci argomentow dla rożnych obiektow lis 5 pyton 2
#atrybuty instancji można definiowac poza definicją klasy np:
b.dlugosc = 10      #atrybut zdefiniowany poza kodem klasy
print(b.dlugosc)
#print(a.dlugosc) nie zadziała  bo atrybuty są w danej instancji obiektu (b) a nie a. NIe są przy pisane do całej klasy
print(a.rodzaj, b.rodzaj)   #wydruk dla instancji 'a' oraz 'b' działa dzięki -->rodzaj = "zwierzę" wynik: zwierzę zwierzę

b.dlugosc = 11      # kolejna zminana atrybutu zdefiniowanego poza kodem klasy
print(b.dlugosc)    # wydruk wartosci atrybutu
a.wiek = 6
print(a.wiek)       # ustalamy wiek lisa - zmiana atrybutu 'wiek' zdef. w kodzie klasy

#atrybuty specjalne dostępne dla wszytskich klas (nie musimy deklarowac)
# np dict ktorego kluczem sa nazwy atrybutow wskazujace na wartosc tych atrybutow
print(a.__dict__)   # {'gatunek': 'lis', 'wiek': 6} obiekt a posiada dwa atrybuty
                    #'gatunek' o wartosci 'lis' i 'wiek' o wartosci '6'
print(b.__dict__)   # 3 atrybuty  {'gatunek': 'pyton', 'wiek': 2, 'dlugosc': 11}

print(Zwierz.__doc__)   # wartosc opisu '''pierwsza klasa''' korzystamy tu z nazwy klasy

#mozna tez skorzystac z nazwy instancji
print(a.__doc__)        # wartosc opisu '''pierwsza klasa'''
