import matplotlib.pyplot as plt
import numpy as np


def approx_function(x, y):
    """ Создание функции аппроксимации """
    t = np.polyfit(x, y, len(x) - 1)        # Вычисление коэффициентов полинома с порядком 13
    f = np.poly1d(t)                        # Создание функции полинома по коэффициентам t
    plt.grid()                              # Генерирование сетки на графике
    x1 = np.linspace(0, 66, 100)            # Генерирование точек области определения x от 0 до 66 на 100 точек
    plt.plot(x1, f(x1), 'r')                # Построение линии функции аппроксимации (красная линия)
    plt.plot(x, y, 'b')                     # Построение графика, содержащий точки, заданные векторами Х и У
    plt.plot(x, y, 'o')                     # Отрисовка точек векторов Х и У
    plt.show()
    print(list(f(x)))
    return list(f(x))                       # Возвращаем список значений фукнции полинома в точках, заданных вектором Х