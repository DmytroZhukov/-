class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setCorrds(self, x, y):
        self.__x = x
        self.__y = y

    def getCorrds(self):
        return self.__x, self.__y


pt = Point(1, 2)
print(pt.getCorrds())
pt.setCorrds(15, 10)
print(pt.getCorrds())
