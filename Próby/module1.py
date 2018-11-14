bajka = "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie!,\nIle cię trzeba cenić, ten tylko się dowie,"
bajka_czysta = bajka.replace("\n"," ").replace(",","").replace(";","").replace("!","")
tekst = bajka_czysta.split(" ")

slownik_dlugosci_wyrazow = {}
for slowo in tekst:
    klucz = len(slowo)
    licznik = 0
    for litera in slowo:
        if litera in 'aeiouyAEIOUY'
            licznik += 1
            if klucz not in slownik_dlugosci_wyrazow:
                slownik_dlugosci_wyrazow[klucz] = []
            slownik_dlugosci_wyrazow[klucz].append(slowo)
print(slownik_dlugosci_wyrazow)
srednia_dl_wyrazu = sum(slownik_dlugosci_wyrazow.keys()) // len(slownik_dlugosci_wyrazow)
komunikat4 = f"średnia długość wyrazu to {srednia_dl_wyrazu} znaków"
print(komunikat4)