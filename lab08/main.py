import numpy as np
import random
import math

australia = []
with open("../australian.dat", "r") as file:
    for line in file:
        australia.append(list(float(x) for x in line.split()))
        # australia.append(list(map(lambda x: float(x), line.split())))

a = australia[0]
b = australia[5]
c = australia[10]
d = australia[20]

# mierzy odleglosc dla n wymiarowego punktu od a do b
def metryka_euklidesowa(a, b):
    c = 0
    length = max(len(a), len(b)) - 1
    for i in range(length):
        element_i = (a[i] - b[i]) ** 2
        c += element_i
    return math.sqrt(c)


# print(metryka_euklidesowa(a, b))
# print(metryka_euklidesowa(a, c))
# print(metryka_euklidesowa(a, d))

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

# print(slownik[0][:5])
# print(slownik[1][:5])
# print(slownik[2][:5])  # KeyError: klucz 2 nie istnieje
# print(list(slownik.values())[1][137])  # [key][nth-element]

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


# def srednia(wektor):
#     n = len(wektor)
#     return np.sum(wektor) / n


# def srednia_lekcja(wektor):
#     n = len(wektor)
#     return np.dot(wektor, np.ones(n)) / n


# def wariancja(wektor):
#     av = srednia(wektor)
#     n = len(wektor)
#     s = av * np.ones(n)
#     u = (wektor - s) ** 2
#     return np.sum(u) / n


# def wariancja_lekcja(wektor):
#     pass


# def odchylenie_std(wektor):
#     return math.sqrt(wariancja(wektor))


# lista = np.array([1, 2, 3, 40])
# """
# print(srednia(lista))
# print(wariancja(lista))
# print(odchylenie_std(lista))
# print(srednia_lekcja(lista))
# """
# test = []
# with open("test.dat", "r") as file:
#     for line in file:
#         test.append(list(map(lambda x: float(x), line.split())))

# # punkty testowe z wykladu: (2,1), (5,2), (7,3), (8,3)
# def linia_trendu():
#     pass


# import math
# import random as rd
# import numpy as np


# def loadData(filename):
#     dane = []

#     with open(filename, "r") as data:
#         for wiersz in data:
#             dane.append(
#                 list(map(lambda e: float(e), wiersz.replace("\n", "").split(" ")))
#             )

#     return dane


# def monte_carlo(function, a, b, pointNum):
#     maxValue = max(map(lambda i: function(i), np.linspace(a, b, pointNum, True)))
#     points = [(rd.uniform(a, b), rd.uniform(0, maxValue)) for x in range(pointNum)]

#     lower = upper = 0
#     for x in points:
#         if x[1] < function(x[0]):
#             lower += 1
#         else:
#             upper += 1

#     return maxValue * (b - a) * (lower / (lower + upper))


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


# filename = "australian.dat"
# data = loadData(filename)
# # result = kolorowanie(data, 2)

# # for x in result:
# #   if x not in data:
# #       print("fail")
# #       break

# print(monte_carlo(math.sin, 0, 1, 10000))
# print(riemann(math.sin, 0, 1, 10000))
# print(trapmann(math.sin, 0, 1, 10000))

# # Oblicz całkę monte-carlo dla funkcji
# # Oblicz całkę riemana dla funkcji

# import math as m

# matrice = []
# with open("australian.dat", "r") as file:
#     matrice = [list(map(lambda a: float(a), line.split())) for line in file]

# matrice_2 = [x[:14] for x in matrice]  # matrice


def srednia_aryt_matrice(lista):
    ones = np.ones((len(lista), 1))
    return float(1 / len(lista)) * np.dot(np.array(lista), ones)[0]


def wariancja_matrice(lista):
    srednia = srednia_aryt_matrice(lista)
    ones = np.ones((1, len(lista))) * srednia
    minus = np.array(lista) - ones
    return float(1 / len(lista)) * np.dot(minus[0], minus[0].T)


def odchylenie_std_matrice(lista):
    return math.sqrt(wariancja_matrice(lista))


# print(srednia_aryt_matrice(matrice_2[0]))
# print(wariancja_matrice(matrice_2[0]))
# print(odchylenie_std_matrice(matrice_2[0]))


# def wariancja():
#     srednia = srednia_aryt_matrice(lista)
#     ones = np.ones((1, len(lista))) * srednia


# import numpy as np


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


# def wariancja(vector):
#     sr = srednia(vector)
#     vector_srednich = sr * np.ones(len(vector))
#     vector_1 = vector - vector_srednich
#     return np.dot(vector_1, vector_1) / len(vector)


# print(wariancja(a))
# print(srednia(a))

print(srednia_aryt_matrice(a))
print(wariancja_matrice(a))
print(odchylenie_std_matrice(a))
