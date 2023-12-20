
class Rectangle:
    def getdata(self,len,bre):
        self.len=len
        self.bre=bre
    def display(self):
          ar=self.len*self.bre
          print("Area:",ar)
I=int(input("enter length"))
L=int(input("enter breadth"))
ob=Rectangle()
ob.getdata(I,L)
ob.display()
