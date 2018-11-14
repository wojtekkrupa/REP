
class Zwierz:
    # poniżej definicja klasy
    # opis klasy
    '''pierwsza klasa'''
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

a = Zwierz("lis", 5, 10)
b = Zwierz("pyton", 2, 5)
c = Zwierz("lis", 3, 10)

#możemy definiować metody na poziomie klas - dot. zwierzeta
a = Zwierz("lis", 3 , 10)		#definiujemy instancję klasy
print(a)					#bez def __str__ __main__.Zwierz object at 0x0000021ED8DD6278> - łańcuch mówiący o typie obiektu
							# a def __str__ lis ma 3 lat/a i osiąga prędkość 10 km/h

# dziedziczenie i definiowanie podklasy
# podklasy służą do pewnego uszczegóławiania obiektów które
# posiadają cechy ogólne zdefiniowane w klasie nadrzędnej jeżeli chcemy aby
# niektóre obiekty posiadały dodatkowe atrybuty i metody

# definiowanie podklasy
class Ptak(Zwierz):
	def __init__(self, gatunek, wiek, predkosc, max_predkosc_lotu, miejsce):
		# wywołujemy metodę klasy nadrzędnej,
		#funkcja super zwraca nam klasę Zwierz i do klasy zwierz wywołujemy jej metodę init
		#przekazujac do niej wymagane argumenty
		super().__init__(gatunek, wiek, predkosc)
		self.predkosc_lotu = max_predkosc_lotu		#atrybuty właściwe tylko dla podklasy
		self.miejsce = miejsce
	def przenies(self):
		if self.miejsce == "klatka":
			self.miejsce = "otwarty"
		else:
			self.miejsce = "klatka"


# deklarujemy pierwszą instancję klasy ptak
p = Ptak("pingwin", 2, 3, 0, "otwarty")		#obiekt pingwin
print(p)		#pingwin ma 2 lat/a i osiąga prędkość 3 km/h to mamy dzięki __str__ z klasy Zwierz po której dziedziczy Ptak

# wyw metodę przenieś
p.przenies()
print(p.miejsce)
p.przenies()
print(p.miejsce)