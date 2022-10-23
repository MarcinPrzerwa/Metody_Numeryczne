import numpy as np

A = np.array([[2,1,5], [4,4,-4], [1,3,1]])
n, m = A.shape
J = np.identity(3)
P = np.identity(n)
L = np.identity(n)
U = A.copy()
PP = np.identity(n)
LL = np.zeros((n,n))
for k in range(0, n - 1):
  index = np.argmax(abs(U[k:,k]))
  index = index + k
  if index != k:
    P = np.identity(n)
    P[[index,k],k:n] = P[[k,index],k:n] #Zamiana macierzy jednostkowej na macierz permutacji, najpierw na pierwszą, potem na drugą
    U[[index,k],k:n] = U[[k,index],k:n] #Przesunięcia wierszy z drugiego na pierwszy i następnie z trzeciego na drugi
    PP = np.dot(P,PP) #Pomnożenie dwóch macierzy permutacji, macierz permutacji końcowa
    LL = np.dot(P,LL)
  L = np.identity(n)
  for j in range(k+1,n):
    L[j,k] = -(U[j,k] / U[k,k])
    LL[j,k] = (U[j,k] / U[k,k])
  U = np.dot(L,U)
LL = LL + J #macierz nie chciała do końca się wypełnic i musiałem dodać macierz jednostkową
PA = np.dot(PP,A)
LU = np.dot(LL,U)

print("A:")
print(A)
print("P:")
print(PP)
print("L:")
print(LL)
print("U:")
print(U)
print("*******************")
print("PA:")
print(PA)
print("LU:")
print(LU)

if np.all(PA)==np.all(LU):
  print("Rozkład macierzy PA=LU jest sobie równy i poprawny.")
else:
  print("PA=LU jest niepoprawne.")
