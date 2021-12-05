from src.Figure import Figure


class Rectangle(Figure):
    name = 'rectangle'

    def __init__(self, param1, param2):
        super().__init__(param1, param2)

    @property
    def perimeter(self):
        return 2 * (self.param1 + self.param2)

    @property
    def area(self):
        return self.param1 * self.param2
