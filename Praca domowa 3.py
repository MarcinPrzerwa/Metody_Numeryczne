import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,0,3], [0,2,0], [3,0,1]])
v = np.array([1,1,1]) #wektor początkowy
#v = np.random.rand(A.shape[0])
n = 20 #liczba kroków
N = np.arange(0,n)
L = []

for  i in range (0,n):
  X=np.matmul(A,v)
  lambd = X[0]
  v = X/lambd
  L.append(lambd)

print('Największa wartość własna: %f' %lambd)
print('Odpowiadający jej wektor własny:')
print(v)

print('Porównanie uzyskanych wyników:')
lin = np.linalg.eig(A)
print(lin)

plt.figure()
plt.xlabel('kroki algorytmu')
plt.ylabel('wartości własne')
plt.title('Wykres kolejnych aproksymacji wartości własnej')
plt.errorbar(N,L, fmt='o', color='r')
plt.show()
