import math

from src.Figure import Figure


class Triangle(Figure):
    name = 'triangle'

    def __new__(cls, param1, param2, param3):
        if (param1 + param2 > param3) and (param1 + param3 > param2) and (param2 + param3 > param1):
            return super().__new__(cls, param1, param2, param3)
        return None

    def __init__(self, param1, param2, param3):
        super().__init__(param1, param2, param3)

    @property
    def perimeter(self):
        return self.param1 + self.param2 + self.param3

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return math.sqrt(
            half_perimeter * (half_perimeter - self.param1) * (half_perimeter - self.param2) * (
                    half_perimeter - self.param3))
