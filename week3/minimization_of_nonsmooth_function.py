import numpy as np
from scipy.optimize import minimize, differential_evolution
from math import sin, exp
import matplotlib.pyplot as plt
"""
Теперь рассмотрим функцию h(x) = int(f(x)) на том же отрезке [1, 30],
т.е. теперь каждое значение f(x) приводится к типу int и функция принимает только целые значения.
"""
def f(x):
    return sin(x / 5.0) * exp(x / 10.0) + 5 * exp(-x / 2.0)

def h(x):
    return int(f(x))

"""
Изучите примеры использования scipy.optimize.minimize в документации Scipy (см. "Материалы")
Попробуйте найти минимум, используя стандартные параметры в функции scipy.optimize.minimize
(т.е. задав только функцию и начальное приближение).
Попробуйте менять начальное приближение и изучить, меняется ли результат.
"""

#print(minimize(h, x0 = 30))

"""
Укажите в scipy.optimize.minimize в качестве метода BFGS (один из самых точных в большинстве случаев градиентных методов оптимизации),
запустите из начального приближения x=2. Градиент функции при этом указывать не нужно – он будет оценен численно.
Полученное значение функции в точке минимума - ваш первый ответ по заданию 1, его надо записать с точностью до 2 знака после запятой
"""

#print(minimize(f, x0 = 2, method = 'BFGS'))

"""
Теперь измените начальное приближение на x=30.
Значение функции в точке минимума - ваш второй ответ по заданию 1,
его надо записать через пробел после первого, с точностью до 2 знака после запятой.
"""

print(minimize(h, x0 = 30, method = 'BFGS'))

bounds = [(1,30)]
print(differential_evolution(h, bounds))
"""
Стоит обдумать полученный результат. Почему ответ отличается в зависимости от начального приближения?
Если нарисовать график функции (например, как это делалось в видео, где мы знакомились с Numpy, Scipy и Matplotlib),
можно увидеть, в какие именно минимумы мы попали.
В самом деле, градиентные методы обычно не решают задачу глобальной оптимизации,
поэтому результаты работы ожидаемые и вполне корректные.
"""
t = np.arange(1,30, 0.1)
gr1 = np.int_(np.sin(t / 5) * np.exp(t / 10) + 5 * np.exp(-t / 2))
#gr1 = int(gr1)
plt.plot(t, gr1)
plt.show()
