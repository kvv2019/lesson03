import abc
from abc import abstractmethod


class Figure(abc.ABC):
    name = 'figure'

    def __new__(cls, *params):
        # Переданные значения должны быть больше нуля
        for param in params:
            if param <= 0:
                return None
        return super().__new__(cls)

    def __init__(self, param1, param2=None, param3=None):
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3

    @property
    @abstractmethod
    def perimeter(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("передан неправильный класс")
        return self.area + figure.area
