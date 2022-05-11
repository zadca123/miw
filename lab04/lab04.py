import math

# https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/australian/
lista = []
with open("../australian.dat", "r") as file:
    for line in file:
        # lista.append(line.split())
        # lista.append(list(map(lambda x: float(x), line.split())))
        lista.append(list(float(x) for x in line.split()))


# lab 4

# # poprawic
def metryka_euklidesowa(arr1, arr2):
    suma = 0
    for i in range(len(arr1) - 1):
        suma += (arr1[i] - arr2[i]) ** 2

    return math.sqrt(suma)


# def metryka_euklidesowa(listaA,listaB):
#     suma = 0
#     for i in range(len(listaA)-1):
#         suma += (listaA[i] - listaB[i]) ** 2
#     return suma ** 0.5

# cos jest zjebane
# row = [1,1,1,1,1,1,1] # cos tam cos tam ten paramatr ma byc listą z jedynkami?
def pary(row, matrix):
    odleglosci = []
    for x in range(len(matrix)):
        klasa_decyzyjna = matrix[x][-1]
        para = klasa_decyzyjna, metryka_euklidesowa(matrix[row], matrix[x])
        odleglosci.append(para)

    return odleglosci

    # row = [1,1,1,1,1,1,1] # cos tam cos tam ten paramatr ma byc listą z jedynkami?
    # wynik = []
    # for item in matrix:
    #     klasa_decyzyjna = item[-1]
    #     odl = metryka_euklidesowa(row,item)
    #     wynik.append(klasa_decyzyjna, odl)
    # return wynik


print(pary(0, lista))

# index = 0
# for para in pary(0,lista):
#     print(index, para)
#     index += 1
# # 0
# # 1
# # 2 -
# # 3 - 0.5


def zad2(x, lista):
    slown = {}
    for para in lista:
        klucz = para[0]
        if klucz in slown:
            slown[klucz].append(para[1])
        else:
            slown[klucz] = []
            slown[klucz].append(para[1])

    return slown


S = zad2(0, lista)
print(S)
# print(zad2(0, pary(0,lista)))

"""
PRACA DOMOWA
zad 1
jak obliczyc metryke euklidesowo dla dwoch obiektów korzystajac z wektorów i operacji na wektorach
"""


def zad3(slownik1, k):
    slownik2 = {1.0: 0, 0.0: 0}
    for key, val in slownik1.values():
        val = val.sort()
        suma = 0
        for i in range(k):
            suma += val[i]
            slownik2[key] = suma

    return slownik2


print(zad3(S, 2))
