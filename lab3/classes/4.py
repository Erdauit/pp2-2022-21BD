class Point():
    def show(self,x,y):
        self.x = x
        self.y = y
        print(x, y)
    def move(self,x,y,x1,y1):
        self.x1 = x1 + x
        self.y1 = y1 + y
        print (x1,y1)

    def dist(self,x,y,x1,y1):
        print(((x1-x)**2  + (y1-y)**2) ** 0.5)

x,y = map(int,input().split())
x1,y1 = map(int,input().split())

Distance = Point()
Distance.show(x,y)
Distance.move(x,y,x1,y1)
Distance.dist(x,y,x1,y1)
        


      
