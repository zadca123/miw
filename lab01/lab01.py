x1: str = "qwe"
x2: int = 123123
x3: float = 123.123
print('1.{0}'.format(type(x1)))
print('2.{0}'.format(type(x2)))
print('3.{0}'.format(type(x3)))

l1: list = ["Nienawidze kota", "Nienawidze psa", "nienawidze czapek", "ale fajno kotak"]
s1: str = " - ".join(l1)
print(s1)
print(s1.split(" - "))

text: str = "i hate the antichrist"
dicc: dict = {"qwe1": 1, "qwe2": 2}
for key, value in dicc.items():
    print(key, value)

zdanie = "Metody Inżynierii Wiedzy są najlepsze"
print(f"{zdanie} ma {len(zdanie)} znaków")
zdanie = zdanie.lower()
zdanie = zdanie.replace("ą", "a").replace("ż","z")
print(f"{zdanie} ma {len(zdanie)} znaków")
print(f"{set(zdanie)} ma długosc {len(set(zdanie))} znaków")

x1: str = "qwe"
x2: int = 123
para: tuple = (x1, x2)
print(f"{para} jest typu {type(para)}")


x1: str = "qwe"
x2: int = 123123
x3: float = 123.123
print('1.{0}'.format(type(x1)))
print('2.{0}'.format(type(x2)))
print('3.{0}'.format(type(x3)))

l1: list = ["Nienawidze kota", "Nienawidze psa", "nienawidze czapek", "ale fajno kotak"]
s1: str = " - ".join(l1)
print(s1)
print(s1.split(" - "))

text: str = "i hate the antichrist"
dicc: dict = {"qwe1": 1, "qwe2": 2}
for key, value in dicc.items():
    print(key, value)

zdanie = "Metody Inżynierii Wiedzy są najlepsze"
print(f"{zdanie} ma {len(zdanie)} znaków")
zdanie = zdanie.lower()
zdanie = zdanie.replace("ą", "a").replace("ż","z")
print(f"{zdanie} ma {len(zdanie)} znaków")
print(f"{set(zdanie)} ma długosc {len(set(zdanie))} znaków")

x1: str = "qwe"
x2: int = 123
para: tuple = (x1, x2)
print(f"{para} jest typu {type(para)}")

l1: list = [1,4,3,4,5]
l2: list = ["a", "b", "c", "d", "e"]
l3: list = l1 + l2
print(l3.index("a"))
l3.append("q")
print(l3)
l3.insert(0, "q")
print(l3)
print(l3.count("q"))
# do domu
# jak obliczyc macierz odwrotna i kiedy mozna ja obliczyc
