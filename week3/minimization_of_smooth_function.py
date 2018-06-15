import numpy as np
from scipy.optimize import minimize
from math import sin, exp
import matplotlib.pyplot as plt
"""
Напишите на Питоне функцию, вычисляющую значение f(x) по известному x.
Будьте внимательны: не забывайте про то, что по умолчанию в питоне целые числа делятся нацело,
и о том, что функции sin и exp нужно импортировать из модуля math.
"""
def f(x):
    return sin(x / 5.0) * exp(x / 10.0) + 5 * exp(-x / 2.0)

"""
Изучите примеры использования scipy.optimize.minimize в документации Scipy (см. "Материалы")
Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize
(т.е. задав только функцию и начальное приближение).
Попробуйте менять начальное приближение и изучить, меняется ли результат.
"""

#print(minimize(f, x0 = 1))

"""
Укажите в scipy.optimize.minimize в качестве метода BFGS (один из самых точных в большинстве случаев градиентных методов оптимизации),
запустите из начального приближения x=2. Градиент функции при этом указывать не нужно – он будет оценен численно.
Полученное значение функции в точке минимума - ваш первый ответ по заданию 1, его надо записать с точностью до 2 знака после запятой
"""

print(minimize(f, x0 = 2, method = 'BFGS'))

"""
Теперь измените начальное приближение на x=30.
Значение функции в точке минимума - ваш второй ответ по заданию 1,
его надо записать через пробел после первого, с точностью до 2 знака после запятой.
"""

print(minimize(f, x0 = 30, method = 'BFGS'))

"""
Стоит обдумать полученный результат. Почему ответ отличается в зависимости от начального приближения?
Если нарисовать график функции (например, как это делалось в видео, где мы знакомились с Numpy, Scipy и Matplotlib),
можно увидеть, в какие именно минимумы мы попали.
В самом деле, градиентные методы обычно не решают задачу глобальной оптимизации,
поэтому результаты работы ожидаемые и вполне корректные.
"""
t = np.arange(1,30, 0.1)
gr1 = np.sin(t / 5) * np.exp(t / 10) + 5 * np.exp(-t / 2)
plt.plot(t, gr1)
plt.show()