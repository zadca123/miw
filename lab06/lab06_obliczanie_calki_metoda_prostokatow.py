import math

"""
# http://specminor.org/2017/01/05/numerical-integration-python.html
# can read this
# https://www.instructables.com/How-to-Make-a-Numerical-Integration-Program-in-Pyt/
"""


def func(x):
    return x
    # return x**3 + 1


def metoda_prostokatow(func, a, b, n=1000):
    ilosc = abs(b - a) / n
    calkowita_powierzchnia = 0
    for i in range(n):
        # pole = (func(a + a + ilosc) / 2) * i
        pole = func(a + a + ilosc) * i
        calkowita_powierzchnia += pole
    return calkowita_powierzchnia


def metoda_trapezow(func, a, b, n=1000):
    ilosc = abs(b - a) / n
    # calkowita_powierzchnia = sum(
    #     (func(a) + func(a + i) * (ilosc / 2)) for i in range(n)
    # )
    # calkowita_powierzchnia = sum(ilosc * func(i) for i in range(n))
    calkowita_powierzchnia = 0
    for i in range(n):
        # pole = (func(a) + func(a + ilosc)) * (i/2)
        pole = (func(a) + func(a + ilosc)) * i
        calkowita_powierzchnia += pole
    return calkowita_powierzchnia


print(metoda_prostokatow(func, 0, 1, 100))
print(metoda_trapezow(func, 0, 1, 100))
