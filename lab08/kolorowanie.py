import math
import random
import numpy as np

australia = []
with open("../../australian.dat", "r") as file:
    for line in file:
        australia.append(list(map(lambda x: float(x), line.split())))

a = australia[0]
b = australia[5]
c = australia[10]
d = australia[20]

# mierzy odleglosc dla n wymiarowego punktu od a do b
def metryka_euklidesowa(a, b):
    # wynik = sum((val1 - val2) ** 2 for val1, val2 in zip(a, b))
    wynik = 0
    dlugosc = max(len(a), len(b)) - 1
    for i in range(dlugosc):
        wynik += (a[i] - b[i]) ** 2

    return math.sqrt(wynik)


def srodek_masy(matrice, klasa):
    najmniejsza_odleglosci_suma = np.inf
    srodek_masy_punkt = matrice[0]
    for i in range(len(matrice)):
        odleglosci_suma = 0
        for j in range(len(matrice)):
            if matrice[j][-1] == klasa:
                odleglosc = metryka_euklidesowa(matrice[j][:-1], matrice[i][:-1])
                odleglosci_suma += odleglosc

        if odleglosci_suma < najmniejsza_odleglosci_suma:
            najmniejsza_odleglosci_suma = odleglosci_suma
            srodek_masy_punkt = matrice[i]

    return srodek_masy_punkt


# print(srodek_masy(australia, 0))
# print(srodek_masy(australia, 1))


def kolorowanie(matrice, ile_klas=2):
    przelacznik = True
    for vec in matrice:
        vec[-1] = random.randint(0, ile_klas - 1)

    while przelacznik:
        przelacznik = False
        srodki_masy = []
        for i in range(ile_klas):
            srodki_masy.append(srodek_masy(matrice, i))

        for vec in matrice:
            metryka_decyzyjna = metryka_euklidesowa(vec[:-1], srodki_masy[0])
            for i in range(ile_klas):
                if metryka_euklidesowa(vec[:-1], srodki_masy[i]) < metryka_decyzyjna:
                    metryka_decyzyjna = metryka_euklidesowa(vec[:-1], srodki_masy[i])
                    vec[-1] = i
                    przelacznik = True

    klasa0 = sum(1 for vec in matrice if vec[-1] == 0)
    klasa1 = sum(1 for vec in matrice if vec[-1] == 1)
    print(f"Liczba klas decyzyjnych 0: {klasa0}")
    print(f"Liczba klas decyzyjnych 1: {klasa1}")
    return matrice


kolorowanie(australia, 2)
