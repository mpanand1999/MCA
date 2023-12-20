class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def display(self):
        ar=self.length*self.breadth
        print("Area:",ar)
#main
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
ob=Rectangle()
ob.getdata(l,b)
ob.display()
