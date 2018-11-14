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

#możemy definiować metody na poziomie klas - dot. zwierzeta
a = Zwierz("lis", 3 , 10)		#definiujemy instancję klasy
print(a)					#bez def __str__ __main__.Zwierz object at 0x0000021ED8DD6278> - łańcuch mówiący o typie obiektu
							# a def __str__ lis ma 3 lat/a i osiąga prędkość 10 km/h

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

	"""polimorfizm związany jest z dziedziczeniem i umożliwia zdefiniowanie w podklasie metod
	które są już zdefiniowane w klasie nadrzędnej tak aby te metody zdefiniowane na nowo, przysłaniały
	metody klasy nadrzędnej"""
	def oblicz_odleglosc(self , czas):	#argumenty jak w klasie nadrzędnej
		#definicja metody
		if self.predkosc_lotu == 0:
			print(czas * self.max_predkosc)	#będziemy korzystać z atrybutu max_predkość
		else:								# w przeciwnym wypadku wyliczamy odl przebytą w powietrzu
			print(czas * self.predkosc_lotu)
# chodzi o to że jeden ptak lata a drugi zasówa po ziemi
p = Ptak("pingwin", 2, 3, 0, "otwarty")
p1 = Ptak("kos", 2, 2, 15, "klatka")
p.oblicz_odleglosc(2)
p1.oblicz_odleglosc(2)