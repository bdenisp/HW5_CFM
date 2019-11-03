'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
'''

import math


# filter
def test_filter():
    assert True

# map

# sorted


# pi from math
def test_pi():
    assert round(math.pi, 5) == 3.14159


# sqrt from math
def test_sqrt():
    assert (math.sqrt(4) ** 2 - 4) < 0.00000001
    assert (math.sqrt(5) ** 2 - 5) < 0.00000001
    assert (math.sqrt(6) ** 2 - 6) < 0.00000001


# pow from math
def test_pow():
    assert math.pow(2, 2) == 4
    assert math.pow(2, 4) == 16
    assert math.pow(13, 2) == 169


# hypot from math
def test_hypot():
    assert (math.hypot(2, 3) ** 2 - 13) < 0.00000000001
    assert (math.hypot(3, 4) ** 2 - 25) < 0.00000000001
    assert (math.hypot(4, 5) ** 2 - 41) < 0.00000000001

