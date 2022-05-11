from pprint import pprint  # ładniejszy print
import numpy as np

# dic = {"polska": "warszawa", "niemcy": "berlin", "rosja": "moskwa",
#        "bialorus": "minsk", "slowacja": "bratyslawa", "czechy": "praga", "ukraina": "kijow", "hiszpania": "madryt"}
# pprint(dic)
# pprint(dic.keys())
# pprint(dic.items())
# pprint(dic.values())
# pprint(sorted(dic.items(), key=lambda x: x[1]))

# print(bool(' '))
# print(bool(''))
# print(bool(0))
# print(bool(1))
# print(bool('1'))
# print(bool('0'))
# print(bool([]))
# print(bool([',']))

# napis = "metody inzynierii wiedzy"
# char = "i"
# if char in napis:
#     print(f"jest {char}")
# else:
#     print(f"nie ma {char}")

# def splitt(napis):
#     lista = []
#     pom = ""
#     for c in napis:
#         if " " == c:
#             lista.append(pom)
#             pom = ""
#         else:
#             pom += c
#     return lista
# print(splitt("qweqwe qwe qweq eqw eqwe qwe"))

passwd = "KochamNauke123123123qw!!!e"
def passwd_checker(passwd) -> bool:
    pom = set()
    if len(passwd) <= 10:
        return False
    if "!" not in passwd:
        return False
    for char in passwd:
        if char.islower():
            pom.add("mala")
        elif char.isupper():
            pom.add("duza")
        elif char.isdigit():
            pom.add("numer")
        if len(pom) == 3:
            return True


    # for char in passwd:
    #     if char.islower():
    #         pom.add("mala")
    #     elif "!" in passwd:
    #         pom.add("!")
    # return "haslo NIE SPELNIA wszystkich warunkow"


print(passwd_checker(passwd))

# listaaa=[1,2,3,4,99]

# for x in listaaa:
#     if x == 99:
#         continue
#     print(x)

# def czynalezy(x,lista):
#     i=0
#     help=False
#     while i < len(lista):
#         if x == lista[i]:
#             help=True
#         i+=1
#     return help

# print(czynalezy(1,listaaa))

# plik=open("txt.txt","r")
# print(plik.read())

# macierz = np.array([[9, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrix = np.linalg.det(macierz)
# print(matrix)
# matrix1 = np.linalg.inv(macierz)
# print(matrix1)
