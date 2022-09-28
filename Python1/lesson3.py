class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width


class Line(Prop):
    def drawLine(self):
        print(
            f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


class Rect(Prop):
    def drawRect(self):
        print(
            f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


l = Line(Point(1, 2), Point(10, 20))
l.drawLine()
r = Rect(Point(30, 40), Point(70, 80))
r.drawRect()
