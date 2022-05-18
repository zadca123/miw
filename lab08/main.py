import numpy as np
import random
import math

australia = []
with open("../australian.dat", "r") as file:
    for line in file:
        australia.append(list(float(x) for x in line.split()))
        # australia.append(list(map(lambda x: float(x), line.split())))

a = australia[0]
b = australia[1]
c = australia[2]
d = australia[3]


def metryka_euklidesowa(v1, v2):
    length = max(len(v1), len(v2)) - 1
    wynik = sum((v1[i] - v2[i]) ** 2 for i in range(length))
    # wynik = sum((a - b) ** 2 for a, b in zip(v1[:-1], v2[:-1]))
    return math.sqrt(wynik)


print("Metryka euklidesowa: ", metryka_euklidesowa(a, b))
print("Metryka euklidesowa: ", metryka_euklidesowa(a, c))
print("Metryka euklidesowa: ", metryka_euklidesowa(a, d))

# 15-wymiarowy punkt x do testów
vec_x = [1 for _ in range(15)]

# "sortuje" wyniki metryki euklidesowej po klasie decyzyjnej w dict (w australian klucze to 0 lub 1)
def slownik_decyzyjny(matrice, x):
    slownik = {}
    for vector in matrice:
        key = vector[-1]
        wynik = metryka_euklidesowa(x, vector)
        slownik.setdefault(key, []).append(wynik)

    return slownik


slownik = slownik_decyzyjny(australia, vec_x)
print("Słownik decyzyjny: ", slownik[0][:3])
print("Słownik decyzyjny: ", slownik[1][:3])

# zwraca liste tupli na wzor: (klasa_decyzyjna, wynik_metryki_euklidesowej)
def mierzymy(x, matrice):
    lista = []
    for vector in matrice:
        wynik = metryka_euklidesowa(x, vector)
        key = vector[-1]
        lista.append((key, wynik))
    return lista


# "sortuje" wyniki metryki euklidesowej po klasie decyzyjnej w dict z listy tupli
def grupujemy(lista_tupli):
    # return {key: value for key, value in lista_tupli}
    slownik = {}
    for tupla in lista_tupli:
        slownik.setdefault(tupla[0], []).append(tupla[1])
    return slownik


pogrupowany_slownik = grupujemy(mierzymy(vec_x, australia))

# zwraca k najmniejszych wartości euklidesowych w postaci słownika z kluczami klas decyzyjnych i sum odleglosci
def suma(slownik, k):
    slownik = {}
    listy = slownik.items()  # zwraca liste tupli na wzor [(key, value)]
    for tupla in listy:
        tupla[1].sort()
        ucieta = tupla[1][:k]
        slownik[tupla[0]] = sum(ucieta)
    return slownik


def dopasuj(slownik):
    print(slownik)
    lista = sorted(slownik.items(), key=lambda x: x[1])
    print(lista)
    if len(lista) == 1:
        return lista[0][0]
    if lista[0][1] == lista[1][1]:
        return None
    else:
        return lista[0][0]


# print(dopasuj(suma(pogrupowany_slownik, 5)))
# print(pogrupowany_slownik)


def metryka_euklidesowa2(a, b):
    a = np.array(a)
    b = np.array(b)
    v = b - a
    return math.sqrt(np.dot(v, v))


# def riemann(function, a, b, precision):
#     points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
#     diff = (b - a) / (precision - 1)

#     area = 0
#     for x in points[1:]:
#         area += diff * x

#     return area


# def trapmann(function, a, b, precision):
#     points = tuple(map(lambda i: function(i), np.linspace(a, b, precision, True)))
#     diff = (b - a) / (precision - 1)

#     area = 0
#     for x in range(1, precision):
#         area += diff * (points[x] + points[x - 1]) / 2

#     return area


# print(monte_carlo(math.sin, 0, 1, 10000))
# print(riemann(math.sin, 0, 1, 10000))
# print(trapmann(math.sin, 0, 1, 10000))

# # Oblicz całkę monte-carlo dla funkcji
# # Oblicz całkę riemana dla funkcji


# def n_kowariancja(macierz):
#     return np.dot(macierz.T, macierz)


# def odwrotnosc_n(macierz):
#     return np.linalg.inv(macierz)


# def lewa_odwrotnosc(macierz):
#     kow = n_kowariancja(macierz)
#     odwrotnosc = odwrotnosc_n(kow)
#     return np.dot(odwrotnosc, macierz.T)


# def srednia(vector):
#     vector_1 = np.ones(len(vector))
#     return np.dot(vector, vector_1) / len(vector)

# print(wariancja(a))
# print(srednia(a))

# print(srednia_arytmetyczna(a))
# print(wariancja(a))
# print(odchylenie_std_matrice(a))
