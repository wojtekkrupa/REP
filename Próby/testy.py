# squares = {1:1,2:4,3:"error",4:16}
# squares[8] = 64
# squares[3] = 9
# print(squares)
#
# primes = {1:2,2:3,4:7,7:17}
# print(primes[primes[4]])

# slowniczek = {'samogloski':['a', 'e', 'i', 'o', 'u', 'y']}
#
# print(len(slowniczek))
# print(slowniczek["samogloski"][2])
#
# #osoby = {"studenci":["Ala", "Jan", "Ania"], "wykladowcy":["doktor", "profesor"]}
# osoby = {"klucz1":["Ala", "Jan", "Ania"], "klucz2":["doktor", "profesor"]}
# print(osoby,"raz")
# #print(osoby["klucz1"][1])
# osoby["klucz2"].append("magister")
# print(osoby, "dwa")
# osoby["administracja"] = ["pani Basia z dziekanatu"]
# print(osoby, "trzy")
# osoby.update({"ochrona":"Impel"})
# print(osoby, "cztery")
# # print(osoby.keys)
# #print(osoby.values)
# for key, item in osoby.items():
#     print(key, item)
#
# print(osoby, "pięć")

slownik = {}
bajka = "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie!,\nIle cię trzeba cenić, ten tylko się dowie,"
bajka_czysta = bajka.replace("\n"," ").replace(",","").replace(";","").replace("!","")
tekst = bajka_czysta.split(" ")
#print(tekst)
# for slowo in (tekst):
#     klucz = len(slowo)
#     if klucz not in wyrazy_wg_długosci:
#        wyrazy_wg_długosci[klucz] = []
#     wyrazy_wg_długosci[klucz].append(slowo)
# print(wyrazy_wg_długosci)
#x = bajka.replace("!", "",)
# slownik = {}
# samogloski = ('a', 'e', 'i', 'o', 'u', 'y')
# ctr = 0
# for slowo in tekst:
#     klucz = slowo
#     if klucz not in slownik:
#         slownik[klucz] = []
#     slownik[klucz].append(slowo)
#     for litera in slowo:
#         if litera in samogloski:
#             ctr =+ 1
#             slownik[klucz].append(ctr)
# print(slownik)
# samogloski = ('a','e','i','o','u','y')

# from collections import Counter
# for slowo in tekst:
#     print(slowo)
#     c = Counter(slowo)
#     for x in samogloski:
#         print(c[x], end=" ")
# c['a']    # count of "a" characters

# def countvowels(znaczki):
#     num_vowels=0
#     for litera in znaczki:
#         if litera in "aeiouAEIOU":
#             num_vowels = num_vowels+1
#         return num_vowels
#
# print(countvowels("ojczyzno"))

for slowo in tekst:
    count = 0

    for char in slowo:

        if char in 'aeiouyAEIOUY':

            count += 1
    print(slowo, end=" ")
    print(count)