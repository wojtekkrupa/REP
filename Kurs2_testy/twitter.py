'''Wewnątrz ciała klasy deklarujemy atrybuty oraz metody.
		atrybuty to zmienne, które będą dostępne dla wszystkich metod naszej Klasy
		metody: własne i
		"magiczne" zaczynające się i kończące "__xyz__" - dwoma podkreśleniami

		metoda od funkcji różni się tym, że metoda jako pierwszy argument przyjmuje self

	unittest - bibl. wbudowana	- testy jednostkowe
	pytest - bibl. zew
	'''
import re


class Twitter(object):
	versja = '1.0'								#przykładowy atrybut-zmienna

	def __init__(self):							#inicjalizator Klasy metoda "magiczna"
		self.tweets = []						#delkarujemy początkową pustą listę tweet'ów - instancja naszej klasy

	def tweet(self, wiadomosc):					#deklarujemy metodę własną z argumentem "wiadomość" - zatweetuj jakąś wiadomość - przekazujemy argument do tej metody
		if len(wiadomosc) > 160:
			raise Exception("wiadomość za długa")			#podstawowa klasa wyjątków
		self.tweets.append(wiadomosc)						#do listy tweetów dołączy wiadomość

	def find_hashtags(self, wiadomosc):
		return re.findall("#(\w+) ", wiadomosc)
