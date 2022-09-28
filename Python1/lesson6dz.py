import math


class Cord:
    __Santim = 1000000

    def __init__(self, line: int):
        if not isinstance(line, int):
            raise ValueError("Сантиметры должны быть целым числом")

        self.__line = line % self.__Santim

    def getFormatSantim(self):
        s = self.__line % 100  # сантиметры
        m = (self.__line % 100) % 10  # метры
        km = (self.__line % 1000) % 100  # километры
        return f"{Cord.__getForm(km)}:{Cord.__getForm(m)}:{Cord.__getForm(s)}"

    @ staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0"+str(x)

    def getMetr(self):
        return self.__line


c1 = Cord(1000)
print(c1.getFormatSantim())
