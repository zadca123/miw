import numpy as np
import math
import matplotlib.pyplot as plt
from pprint import pprint
from itertools import combinations
import random


class Wektor:
    def __init__(self, a, b, grupa="gr1"):
        self.a = np.array(a)
        self.b = np.array(b)
        self.odleglosc = self.metryka_euklidesowa()
        self.suma = 0
        self.grupa = grupa

    def wyznacznik(self):
        return np.linalg.det(self.a, self.b)

    def metryka_euklidesowa(self):
        v = self.b - self.a
        return math.sqrt(np.dot(v, v))


class Data:
    def __init__(self, dataset=None, filename="../australian.dat"):
        self.filename = filename
        self.dataset = dataset or self.load_file()

        self.comb_data = list(combinations(self.dataset, 2))
        self.odleglosci = list(Wektor(vec1, vec2) for vec1, vec2 in self.comb_data)
        self.dicc = self.set_sums()

        self.grupy = self.podziel_na_grupy()
        self.grupy_comb = self.podziel_na_comb_grupy()
        self.grupy_odleglosci = self.oblicz_odleglosci_w_grupach()

        # self.odleglosci = self.oblicz_odleglosci()
        # self.dicc = self.set_sums2()

    def podziel_na_grupy(self):
        random.shuffle(self.dataset)
        dl = int(len(X) / 2)
        return {"gr1": X[:dl], "gr2": X[dl:]}

    def podziel_na_comb_grupy(self):
        result = {}
        for key, value in self.grupy.items():
            result.update({key: tuple(combinations(value, 2))})
        return result

    def oblicz_odleglosci_w_grupach(self):
        result = []
        for key, values in self.grupy_comb.items():
            for pkt in values:
                result.append(Wektor(pkt[0], pkt[1], grupa=key))
        return result

    def load_file(self):
        dataset = []
        with open(self.filename, "r") as file:
            for line in file:
                dataset.append(tuple(float(x) for x in line.split()))
                # dataset.append(list(float(x) for x in line.split()))
                # self.dataset.append(list(map(lambda x:float(x),line.split())))
        return dataset

    def metryka_euklidesowa(self, a, b):
        suma = 0
        for i in range(len(self.dataset) - 1):
            suma += (b[i] - a[i]) ** 2
        return math.sqrt(suma)

    # dict({(vec1, vec2): 1} for vec1, vec2 in self.comb)
    def oblicz_odleglosci(self):
        result = {}
        for pkt1, pkt2 in self.comb:
            result.update({(pkt1, pkt2): self.metryka_euklidesowa(pkt1, pkt2)})
        return result

    def set_sums(self):
        dicc = {}
        for vec in self.odleglosci:
            key1 = tuple(vec.a)
            key2 = tuple(vec.b)
            dicc.setdefault(key1, 0)
            dicc.setdefault(key2, 0)
            dicc[key1] += vec.odleglosc
            dicc[key2] += vec.odleglosc
        return dicc

    def set_sums2(self):
        dicc = {}
        for vec, odl in self.odleglosci.items():
            key1 = tuple(vec[0])
            key2 = tuple(vec[1])
            dicc.setdefault(key1, 0)
            dicc.setdefault(key2, 0)
            dicc[key1] += odl
            dicc[key2] += odl
        return dicc

    def minimal(self):
        minimal = self.grupy_odleglosci[0]
        # print(minimal)
        for vec in self.grupy_odleglosci:
            if vec.odleglosc < minimal.odleglosc:
                minimal = vec
        return minimal

    def get_min(self):
        minimal = min(self.dicc.values())
        for key, val in self.dicc.items():
            if val == minimal:
                return (key, val)

    def plot_figure(self):
        x, y = zip(*self.dicc.items())
        plt.plot(x, y, "r*")
        # x, y = zip(*self.dicc2.items())
        # plt.plot(x, y, "r*")
        # plt.plot(self.dataset, "r*")
        plt.show()


X = [
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [7, 7],
    [8, 8],
    [9, 9],
    [10, 10],
    [11, 11],
    [12, 12],
    [13, 13],
]
data = Data(X)
# print(data.get_min())
# print(data.grupy)
# print(data.grupy_comb)
# print(data.oblicz_odleglosci_w_grupach())
# print(data.dicc2)
print(data.minimal().a)
print(data.minimal().b)
print(data.minimal().grupa)
print(data.minimal().odleglosc)

# print(data.dataset)
# print(data.comb_data)


# data.plot_figure()
# print(data.dicc)
# for i in data.odleglosci:
#     print(i.a, i.b, i.odleglosc)


"""TODO
wagi kropek

funkcja1_oblicz_waga_kropek()
funkcja2_waga_kropek()
funkcja3_minimum_waga(zrior_kropek)
funkcja4_srodek_ciezkosci(zrior_kropek)
28 luty 1:10 na wykladzie
"""
