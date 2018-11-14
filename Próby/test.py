def append_to_file(file_name, lines):
    """"
    Funkcja dodająca linijkę do pliku o podanej nazwie
    """
    with open(file_name, 'w') as f:
        f.writelines(lines)

sciezka_nazwa_pliku_zrodlo = 'inwokacja.txt'
sciezka_nazwa_pliku_wynik = 'inwokacja_stats.txt'

with open(sciezka_nazwa_pliku_zrodlo, 'r') as plik_zrodlowy:
    tekst = plik_zrodlowy.read()
    tekst_maly = tekst.lower()
    tekst_podzielony = tekst_maly.split(' ')

    ile_wyrazow = len(tekst_podzielony)
    komunikat1 = f"Ilość wyrazów to {ile_wyrazow}"
    # print(komunikat1)

    ile_znakow = len(tekst)
    komunikat2 = f"Dlugość tekstu to {ile_znakow} znaków"
    # print(komunikat2)

    slownik_dlugosci_wyrazow = {}
    for slowo in tekst_podzielony:
        klucz = len(slowo)
        if klucz not in slownik_dlugosci_wyrazow:
            slownik_dlugosci_wyrazow[klucz] = []
        slownik_dlugosci_wyrazow[klucz].append(slowo)

    srednia_dl_wyrazu = sum(slownik_dlugosci_wyrazow.keys()) // len(slownik_dlugosci_wyrazow)
    komunikat4 = f"średnia długość wyrazu to {srednia_dl_wyrazu} znaków"
    # print(komunikat4)

    append_to_file(sciezka_nazwa_pliku_wynik,
                   komunikat1+'\n'+
                   komunikat2+'\n'+
                   komunikat4)

    slownik_samogloski = {}
    samogloski = ('a', 'e', 'i', 'o', 'u', 'y')
    for slowo in tekst_podzielony:
        # print(slowo, end=' ')
        for element in samogloski:
            klucz1 = element
            x = slowo.count(element)
            slownik_samogloski[klucz1].append(x)
            print(slownik_samogloski)
            #print(slowo.count(element))
