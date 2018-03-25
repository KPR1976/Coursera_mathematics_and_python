import numpy as np
import scipy.linalg as scl
from math import sin, exp
import matplotlib.pyplot as plt

fx = lambda x: sin(x / 5.0) * exp(x / 10.0) + 5 * exp(-x / 2.0)

#first degree polynomial
a = [[1, 1], [1, 15]]
b = [fx(1), fx(15)]
x1 = scl.solve(a, b)
print(x1)
t = np.linspace(0.75, 15.75)
gr1 = np.sin(t / 5) * np.exp(t / 10) + 5 * np.exp(-t / 2)
gr2 = x1[0] + x1[1] * t
plt.plot(t,gr1,'b')
plt.plot(t,gr2,'r')
plt.show()

#second degree polynomial
a = [[1, 1, 1], [1, 8, 64], [1, 15, 225]]
b = [fx(1), fx(8), fx(15)]
x2 = scl.solve(a, b)
print(x2)
gr3 = x2[0] + x2[1] * t + x2[2] * t * t
plt.plot(t,gr1,'b')
plt.plot(t,gr2,'r')
plt.plot(t,gr3,'g')
plt.show()

#third degree polynomial
a = [[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]]
b = [fx(1), fx(4), fx(10), fx(15)]
x3 = scl.solve(a, b)
print(scl.solve(a, b).round(2))

gr4 = x3[0] + x3[1] * t + x3[2] * t * t + x3[3] * t ** 3

plt.plot(t,gr1,'b')
plt.plot(t,gr2,'r')
plt.plot(t,gr3,'g')
plt.plot(t,gr4,'c')
plt.show()
