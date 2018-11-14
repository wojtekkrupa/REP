def append_to_file(file_name, lines):
    """"
    Funkcja dodająca linijkę do pliku o podanej nazwie
    """
    with open(file_name, 'w') as f:
        f.writelines(lines)

sciezka_nazwa_pliku_zrodlo = 'inwokacja.txt'
sciezka_nazwa_pliku_wynik = 'inwokacja_stats.txt'

with open(sciezka_nazwa_pliku_zrodlo, 'r') as plik_zrodlowy:
    tekst = plik_zrodlowy.read().replace("\n"," ").replace(",","").replace(";","").replace("!","")
    tekst_maly = tekst.lower()
    tekst_podzielony = tekst_maly.split(' ')

    ile_wyrazow = len(tekst_podzielony)
    komunikat1 = f"Ilość wyrazów to {ile_wyrazow}"
    # print(komunikat1)

    ile_znakow = len(tekst_maly)
    komunikat2 = f"Dlugość tekstu to {ile_znakow} znaków"
    # print(komunikat2)
    # ----------------------------------------------------------------------------------------
    # from collections import defaultdict
    # wyrazy_wg_długosci = defaultdict(list)
    # for slowo in (tekst_podzielony):
    #     wyrazy_wg_długosci[key].append(slowo)
    # print(wyrazy_wg_długosci)
    # ----------------------------------------------------------------------------------------
    wyrazy_wg_długosci = {}
    for slowo in (tekst_podzielony):
        klucz = len(slowo)
        if klucz not in wyrazy_wg_długosci:
            wyrazy_wg_długosci[klucz] = []
        wyrazy_wg_długosci[klucz].append(slowo)
    print(wyrazy_wg_długosci)
    srednia_dl_wyrazu = sum(wyrazy_wg_długosci.keys()) // len(wyrazy_wg_długosci)
    komunikat4 = f"średnia długość wyrazu to {srednia_dl_wyrazu} znaków"
    #print(komunikat4)
    # ----------------------------------------------------------------------------------------
    # slownik_dlugosci_wyrazow = {}
    # for slowo in tekst_podzielony:
    #     klucz = len(slowo)
    #     if klucz not in slownik_dlugosci_wyrazow:
    #         slownik_dlugosci_wyrazow[klucz] = []
    #     slownik_dlugosci_wyrazow[klucz].append(slowo)
    #
    # srednia_dl_wyrazu = sum(slownik_dlugosci_wyrazow.keys()) // len(slownik_dlugosci_wyrazow)
    # komunikat4 = f"średnia długość wyrazu to {srednia_dl_wyrazu} znaków"
    # print(komunikat4)
    # ----------------------------------------------------------------------------------------
    append_to_file(sciezka_nazwa_pliku_wynik,
                   komunikat1+'\n'+
                   komunikat2+'\n'+
                   komunikat4)
    # ----------------------------------------------------------------------------------------
    # slownik_slow_z_samogloskami = {}
    # for slowo in tekst_podzielony:
    #     licznik = 0
    #
    #     for litera in slowo:
    #
    #         if litera in 'aeiouy':
    #             licznik += 1
    #     print(slowo, end=" ")
    #     print(licznik)
    #
    #     if licznik not in slownik_slow_z_samogloskami:
    #         slownik_slow_z_samogloskami.append(slowo)

