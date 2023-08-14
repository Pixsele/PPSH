class GeometricFigures():
    def __init__(self, figures):
        self.figures = figures

    def get_perimeter(self):
        raise SyntaxError

    def get_all_perimeters(self):
        for figure in self.figures:
            print(figure.get_perimeter())


class Triangle(GeometricFigures):
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def get_perimeter(self):
        return f'Переиметр = {self.a1 + self.a2 + self.a3}.'

    def __str__(self):
        return f'Треугольник со сторонами : {self.a1},{self.a2},{self.a3}.'


class Square(GeometricFigures):
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return f'Переиметр = {self.a * 4}.'

    def __str__(self):
        return f'Квадрат со стороной : {self.a}.'


class Rectangle(GeometricFigures):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_perimeter(self):
        return f'Переиметр =  {(self.a + self.b) * 2}.'

    def __str__(self):
        return f'Прямоугольник со сторонами : {self.a},{self.b}.'


figures = [Triangle(1, 2, 3), Triangle(4, 5, 6), Square(10), Square(20), Rectangle(6, 7), Rectangle(7, 8)]

for figure in figures:
    print(figure, figure.get_perimeter())
