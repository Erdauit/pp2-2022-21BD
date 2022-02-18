class Myclass:

    def getstring(self):
        self.s = input()
    def printstring(self):
        print(self.s.upper())

a = Myclass()
a.getstring()
a.printstring()