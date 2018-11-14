'''
listy i krotki
'''

lista = [1,2,'element',3.14]	#lista jest zmienna, nawias kwadratowy
# długosc_listy = len(lista)	#pod zmianną zapamiętana ilość elementów listy
# print('to jest lista:',lista)
# print('lista ma długość', długosc_listy, '- od 0 do ', (długosc_listy - 1))
#
# pozycja_listy = int(input('podaj pozycję do sprawdzenia : '))
# print('pod pozycją {} znajduje się : ' .format(pozycja_listy), lista[pozycja_listy])
# #print(lista[pozycja_listy])

print()

krotka=(1,2,'element', 3.14)			#krotki są niezmienne jak łańcuchy, nawias zwykły
print('to jest krotka: ',krotka)


print(krotka[1], '- to jest 2 element krotki czyli druga pozycja, wpisany kod: "krotka[1]"')		#drugi element krotki
print(3 in krotka)		#czy element znajduje się w krotce - wynik to boolean
print(lista[1:2], 'podałem lista[1:2]')
print(lista[1], '  podałem lista[1]')
print(krotka[:-2], 'podałem krotka[:-2]')		#wyświetla elementy od 0 do -2, czyli od początku z pominięciem dwóch ostatnich pozycji
