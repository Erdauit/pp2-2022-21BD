from cmath import rect


class Shape():
    def areas(self):
        print(0)

class rectangle(Shape):
    def __init__ (self, length, width):
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
 
l = int(input())
r = int(input())

Area= rectangle(l)
Area.area()
