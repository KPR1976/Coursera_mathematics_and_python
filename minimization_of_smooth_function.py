import numpy as np
from scipy.optimize import minimize
from math import sin, exp
import matplotlib.pyplot as plt
"""
Напишите на Питоне функцию, вычисляющую значение f(x) по известному x. Будьте внимательны: не забывайте про то, что по умолчанию в питоне целые числа делятся нацело, и о том, что функции sin и exp нужно импортировать из модуля math.
"""
def f(x):
    return sin(x / 5.0) * exp(x / 10.0) + 5 * exp(-x / 2.0)

x
res = f(x)
print(res)
