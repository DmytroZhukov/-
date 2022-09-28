import math


class Стол:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Столы:
    def __init__(self, sp: Стол, ep: Стол, color: str = "Крассный", width: str = "1 шт."):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width


class Прямоугольный(Столы):
    def drawone(self):
        print(
            f"Прямоугольный стол: {self._sp}, {self._ep}, {self._color}, {self._width}")


class rectangle(Прямоугольный):
    def __init__(self, breadth, length):
        self.breadth = breadth
        self.length = length

    def area(self):
        return self.breadth * self.length


a = int(input("Введите длину прямоугольника: "))
b = int(input("Введите ширину прямоугольника: "))
obj = rectangle(a, b)
print("Площадь прямоугольника:", obj.area())

print()


class Круглый(Столы):
    def drawtwo(self):
        print(
            f"Круглый стол: {self._ep}, {self._color}, {self._width}")


class circle(Круглый88):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius


r = int(input("Введите радиус круга: "))
obj = circle(r)
print("Площадь круга:", round(obj.area(), 2))
print("Длина окружности:", round(obj.perimeter(), 2))

one = (Прямоугольный(Стол(10, 10), Стол(20, 20)))
one.drawone()

two = (Круглый(Стол(15, 15), Стол(15, 15)))
two.drawtwo()
