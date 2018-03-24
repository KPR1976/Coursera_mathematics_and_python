import numpy as np
import scipy.linalg as scl
from math import sin, exp
import matplotlib.pyplot as plt

fx = lambda x: sin(x / 5.0) * exp(x / 10.0) + 5 * exp(-x / 2.0)

#first degree polynomial
a = [[1, 1], [1, 15]]
b = [fx(1), fx(15)]
print(scl.solve(a, b))
plt.plot(a,b)
plt.show()
#second degree polynomial
a = [[1, 1, 1], [1, 8, 64], [1, 15, 225]]
b = [fx(1), fx(8), fx(15)]
print(scl.solve(a, b))
plt.plot(a,b)
plt.show()
#third degree polynomial
a = [[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]]
b = [fx(1), fx(4), fx(10), fx(15)]
print(scl.solve(a, b).round(2))
plt.plot(a,b)
plt.show()
print(fx(1), fx(4), fx(10), fx(15))
