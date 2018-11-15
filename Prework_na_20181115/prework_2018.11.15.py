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

    # ----------------------------------------------------------------------------------------
    slowa_o_2_lub_wiecej_samogloskach = {}
    for slowo in tekst_podzielony:
        count = 0
        for litera in slowo:
            if litera in 'aeiouy':
                count += 1
        if count >= 2:
            slowa_o_2_lub_wiecej_samogloskach[slowo] = count

    wyrazy_z_samogloskami = (len(slowa_o_2_lub_wiecej_samogloskach))
    komunikat3 = f"{wyrazy_z_samogloskami} wyrazów zawiera co najmniej dwie samogłoski"

    # ----------------------------------------------------------------------------------------
    wyrazy_wg_dlugosci = {}
    for slowo in (tekst_podzielony):
        klucz = len(slowo)
        if klucz not in wyrazy_wg_dlugosci:
            wyrazy_wg_dlugosci[klucz] = []
        wyrazy_wg_dlugosci[klucz].append(slowo)

    srednia_dl_wyrazu = sum(wyrazy_wg_dlugosci.keys()) // len(wyrazy_wg_dlugosci)
    komunikat4 = f"średnia długość wyrazu to {srednia_dl_wyrazu} znaków"

    # ----------------------------------------------------------------------------------------
    append_to_file(sciezka_nazwa_pliku_wynik,
                   komunikat1 +'\n' +
                   komunikat2 +'\n' +
                   komunikat3 +'\n' +
                   komunikat4)
