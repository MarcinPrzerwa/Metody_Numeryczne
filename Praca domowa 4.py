import numpy as np
import matplotlib.pyplot as plt

xs = np.array([1,2,3,4,5])
ys = np.array([1,4,-6,-3,6])

def funkcja(x, y):
  n = len(x)
  r = []
  for i in range(n):
        r.append(y[i])
  for j in range(1, n):
    for i in range(n-1, j-1, -1):
      r[i] = float(r[i]-r[i-1])/float(x[i]-x[i-j])
  return np.array(r)

def funkcjaD(x,x1):
  a = funkcja(xs,ys)
  b=0
  for i in range(0,len(a)):
    c=1
    if i==0:
      b+=a[0]
      continue
    else:
      for j in range(0,i):
        c=c*(x-x1[j])
    b+=c*a[i]
  return b

print("Współczynniki wielomianu Newtona:")
print(funkcja(xs,ys))
#t = float(input("wartość wielomianu interpolacyjnego dla podanego punktu x: "))
print("Wartość wielomianu interpolacyjnego dla punktu x=3:")
print(funkcjaD(3,xs))

x3 = np.arange(0,6,0.1)

plt.plot(x3,funkcjaD(x3,xs))
plt.errorbar(xs,ys,fmt="o",color='r')
plt.show()