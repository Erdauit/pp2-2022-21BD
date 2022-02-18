class Shape():
    def areas(self):
        print(0)

class Square(Shape):
    def __init__ (self, length):
        self.length = length
    def area(self):
        print(pow(self.length,2))
 
l =int(input())

Area= Square(l)
Area.area()

