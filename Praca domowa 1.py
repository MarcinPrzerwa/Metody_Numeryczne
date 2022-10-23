# Metoda Bisekcji
import matplotlib.pyplot as plt
import numpy as np


def f(X, n):  # Do wprowadzania funkcji z klawiatury
    x = X
    return eval(n)

print('Napisz wybraną funkcję w celu znalezienia miejsca zerowego')
print('(Na przykład: 2x-3)')

y = input('Funkcja: ')
x = np.linspace(-10, 10)
plt.figure()  # pierwszy wykres
plt.grid(ls='--')
plt.axhline(y=0, color="#000000")
plt.axvline(x=0, color="#000000")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x, f(x, y))
#plt.show()

print("Podaj krańce przedziału i jej dokładność")
a = float(input('minimum:'))
b = float(input('maksimum: '))
dok = float(input('dokładność: '))

if a > b:  # gdyby użytkownik się pomylił
    a, b = b, a

i = 0
A = []  # aproksymacja
B = []  # kolejny krok algorytmu
x0 = a + (b - a) / 2

deltaX = []  # błąd bezwzględny
while abs(f(x0, y)) > dok:
    i += 1
    if np.sign(f(x0, y)) == np.sign(f(a, y)):
        a = x0
    elif np.sign(f(x0, y)) == np.sign(f(b, y)):
        b = x0
    x0 = a + (b - a) / 2
    B.append(i)
    A.append(x0)
    deltaX.append(abs((b - a) / 2))

print("Miejsce zerowe: %f" % x0)

plt.figure()  # drugi wykres
plt.plot(B, A)
plt.errorbar(B, A, yerr=deltaX, ecolor='red', capsize=2, fmt='o')
plt.grid(ls='--')
plt.xlabel('kolejne kroki algorytmu')
plt.ylabel('aproksymacja miejsca zerowego')
plt.show()