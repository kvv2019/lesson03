from src.Figure import Figure


class Square(Figure):
    name = 'square'

    def __init__(self, param1):
        super().__init__(param1)

    @property
    def perimeter(self):
        return self.param1 * 4

    @property
    def area(self):
        return self.param1 ** 2
