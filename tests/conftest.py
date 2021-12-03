import math
import random

import pytest

from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle


def rnd_value():
    return (lambda x: 0.1 if x == 0 else x)(random.random())


@pytest.fixture
def figure_reg(test_figure, test_param1, test_param2, test_param3):
    if issubclass(test_figure, Circle) or issubclass(test_figure, Square):
        return test_figure(test_param1)
    elif issubclass(test_figure, Rectangle):
        return test_figure(test_param1, test_param2)
    elif issubclass(test_figure, Triangle):
        return test_figure(test_param1, test_param2, test_param3)


@pytest.fixture
def figure_rnd(test_figure):
    if issubclass(test_figure, Circle) or issubclass(test_figure, Square):
        return test_figure(rnd_value())
    elif issubclass(test_figure, Rectangle):
        return test_figure(rnd_value(), rnd_value())
    elif issubclass(test_figure, Triangle):
        param1 = rnd_value()
        param2 = rnd_value()
        param3 = math.sqrt(param1 ** 2 + param2 ** 2 - 2 * param1 * param2 * math.cos(random.randint(1, 179)))
        return test_figure(param1, param2, param3)


@pytest.fixture
def circle_rnd():
    return Circle(rnd_value())


@pytest.fixture
def square_rnd():
    return Square(rnd_value())


@pytest.fixture
def rectangle_rnd():
    return Rectangle(rnd_value(), rnd_value())


@pytest.fixture
def triangle_rnd():
    param1 = rnd_value()
    param2 = rnd_value()
    param3 = math.sqrt(param1 ** 2 + param2 ** 2 - 2 * param1 * param2 * math.cos(random.randint(1, 179)))
    return Triangle(param1, param2, param3)
