''' metody klas, jak definiować metody klas
są to funkcje które można wywoływać z poziomu klasy. mogą dotyczyć samej klasy lub poszczególnych instancji '''

class Zwierz:
    # poniżej definicja klasy
    # opis klasy
    '''pierwsza klasa'''
    # definiujemy metodę klasy czyli funkcję wewnątrz klasy
    #rodzaj          # definiujemy atrybuty ktorych warotci beda wspolne dla wszytskich obiektow klas
    rodzaj = "zwierzę"             # w tym celu wpisujemy nazwę atrybutu wewnątrz defnicji klasy pomijając "self"
    zwierzeta = {}					#nowa zmienna - słownik którego kluczem będą nazwy zwierząt a wartością liczebność

    def __init__(self, gatunek, wiek, predkosc):    #po self podajemy argumenty ktore będziemy podawawac przy tworzeniu instancji klas
        self.gatunek = gatunek                      #podczas inicjalizacji klasy stawiamy atrybuty
        self.wiek = wiek
        self.max_predkosc = predkosc			#kolejny atrybut potrzebny w metodzie
        if gatunek in Zwierz.zwierzeta:			#jeśli gatunek znajduje się w słowniku zwierzęta
            Zwierz.zwierzeta[gatunek]+= 1		# to dodajmy 1 do wartości wskazywanej przez ten gatunek zwiększając liczebność zwierząt w naszym zoo
        else:									# w przeciwnym razie tworzymy nowy wpis w słowniku dodając taki gatunek i ustaw liczebność na 1
            Zwierz.zwierzeta[gatunek] = 1
    def oblicz_odleglosc(self, czas):			#metody dostępne (wywoływane) z poziomu instancji powinny posiadać argument self
        print(czas * self.max_predkosc)
    def wypisz_zwierzeta():				#kolejna metoda klasy (bez self) wypisująca ilość
        print(Zwierz.zwierzeta)
# metoda specjalna klasy wywoływane prez python'a w chwili wywoływania funkcji wbudowanych np. print
    def __str__(self):
        return self.gatunek\
			   + " ma " + str(self.wiek)\
			   + " lat/a i osiąga prędkość "\
			   + str(self.max_predkosc) + " km/h"
#w powyższym str - wiek i str max.predkosc bo są intiger'ami

Zwierz.wypisz_zwierzeta()		#sprawdzenie zawartości słownika przed deklaracją obiektów {}
a = Zwierz("lis", 5, 10)
b = Zwierz("pyton", 2, 5)
c = Zwierz("lis", 3, 10)
Zwierz.wypisz_zwierzeta()		# {'lis': 2, 'pyton': 1} mamy 2 obiekty gatunku lis - sprawdzenie po deklaracji
a.oblicz_odleglosc(2)
b.oblicz_odleglosc(2)

#możemy definiować metody na poziomie klas - dot. zwierzeta
a = Zwierz("lis", 3 , 10)		#definiujemy instancję klasy
print(a)					#bez def __str__ __main__.Zwierz object at 0x0000021ED8DD6278> - łańcuch mówiący o typie obiektu
							# a def __str__ lis ma 3 lat/a i osiąga prędkość 10 km/h