import math


class Point2D:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def pointPrint(self):
        print("x={},y={}".format(self.__x, self.__y))


p1 = Point2D(x=30, y=40)
p2 = Point2D(x=80, y=90)

p1.pointPrint()
p2.pointPrint()


class LineDraw():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


li = LineDraw(p1, p2)
li.p1.pointPrint()
li.p2.pointPrint()

x = p1.getX() - p2.getX()
y = p1.getY() - p2.getY()

c = math.sqrt((x * x) + (y * y))
c1 = math.sqrt(math.pow(x, 2) + (y * y))
print(c)
print(c1)
