class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.__value = value

    def __delete__(self, obj):
        del self.__value


class Point:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y


pt = Point(1, 2)
pt.coordX = 5
pt.coordY = 10
print(pt.coordX, pt.coordY)
