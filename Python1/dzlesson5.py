class Point:
    def __init__(self, x=0, y=0, z=0, d=0, f=0):
        self.__x = x
        self.__y = y
        self.__z = z
        self.__d = d
        self.__f = f

    def __str__(self):
        return f"({self.__x}, {self.__y}, {self.__z})"


class Amd:
    def __init__(self):
        print("Процессор AMD")
        # super().__init__()


class Intell:
    def __init__(self):
        print("Процессор Intell")
        # super().__init__()


class Cpu(Amd, Intell):
    def __init__(self, sp: Point, ep: Point, dp: Point, color: str = "red", width: int = 2):
        self._sp = sp
        self._ep = ep
        self._dp = dp
        self._color = color
        self._width = width
        # super().__init__()

    def darw1(self):
        print(
            f"Характенистики материнки: {self._sp}, {self._ep}, {self._dp}, {self._color}, {self._width}")


class NVidia:
    def __init__(self):
        print("Видеокарта NVidia")
        # super().__init__()


class GeForce:
    def __init__(self):
        print("Видеокарта GeForce")
        # super().__init__()


class Gpu(NVidia, GeForce):
    def __init__(self):
        print("Графический процессор")
        # super().__init__()


class Memory:
    def __init__(self):
        print("Память")
        # super().__init__()


class Matherboard(Cpu, Gpu, Memory):
    def __init__(self, sp: Point, ep: Point, dp: Point, color: str = "black", width: int = 3):
        self._sp = sp
        self._ep = ep
        self._dp = dp
        self._color = color
        self._width = width
        # super().__init__()

    def darw(self):
        print(
            f"Характенистики: {self._sp}, {self._ep}, {self._dp}, {self._color}, {self._width}")


l = Matherboard(Point(10, 10, 10), Point(100, 100, 100), "green", 5)
l.darw()
p = Cpu(Point(10, 10, 10), Point(123, 124, 125), "black", 2048)
p.darw1()
# print(Matherboard.__mro__)
