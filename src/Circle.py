import math

from src.Figure import Figure


class Circle(Figure):
    name = 'circle'

    def __init__(self, param1):
        super().__init__(param1)

    @property
    def perimeter(self):
        return 2 * math.pi * self.param1

    @property
    def area(self):
        return math.pi * (self.param1 ** 2)
