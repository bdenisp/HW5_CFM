'''
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
'''

import math


# filter
def test_filter():
    assert list(filter(lambda x: x[1] == 'e', ['leo', 'lao', 'luo', 'lio', 'leo'])) == ['leo', 'leo']
    assert list(filter(lambda x: x == 'leo', ['leo', 'lao', 'luo', 'lio', 'leo'])) == ['leo', 'leo']


# map
def test_map():
    assert list(map(lambda x: x.upper(), ['leo', 'lao', 'luo', 'lio', 'leo'])) == ['LEO', 'LAO', 'LUO', 'LIO', 'LEO']
    assert list(map(int, [1.0, 2.0, 3.0])) == [1, 2, 3]


# sorted
def test_sorted():
    assert list(sorted(['leo', 'lao', 'luo', 'lio', 'leo'], key=lambda x: x[1])) == ['lao', 'leo', 'leo', 'lio', 'luo']
    assert list(sorted(['leo', 'lao', 'luo', 'lio', 'leo'], key=lambda x: x[1], reverse=True)) == ['luo', 'lio', 'leo',
                                                                                                   'leo', 'lao']


# pi from math
def test_pi():
    assert round(math.pi, 5) == 3.14159


# sqrt from math
def test_sqrt():
    assert (math.sqrt(4) ** 2 - 4) < 0.00000000001
    assert (math.sqrt(5) ** 2 - 5) < 0.00000000001
    assert (math.sqrt(6) ** 2 - 6) < 0.00000000001


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
