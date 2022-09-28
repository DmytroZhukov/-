class Lolo:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    # def isDigit(self):
    #     if (isinstance(self.__x, int) or isinstance(self.__x, float)) and \
    #             (isinstance(self.__y, int) or isinstance(self.__y, float)):
    #         return True
    #     return False

    # def isInt(self):
    #     if isinstance(self.__x, int) and isinstance(self.__y, int):
    #         return True
    #     return False


class Prop:
    def __init__(self, sp: Lolo, ep: Lolo, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width


class Line(Prop):
    def draw(self):
        print(
            f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Prop):
    def draw(self):
        print(
            f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Ellipse(Prop):
    def draw(self):
        print(
            f"Рисование элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")


figs = []
figs.append(Line(Lolo(0, 0), Lolo(10, 10)))
figs.append(Line(Lolo(10, 10), Lolo(20, 10)))
figs.append(Rect(Lolo(50, 50), Lolo(100, 100)))
figs.append(Ellipse(Lolo(-10, -10), Lolo(10, 10)))

for f in figs:
    f.draw()
