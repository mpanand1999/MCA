class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print("Area:",ar)
        return ar
    def perimeter(self):
        per=2*(self.length+self.breadth)
        print("Perimeter:",per)
        
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
ob1=Rectangle()
ob1.getdata(l,b)
ob1.area()
ob1.perimeter()

l1=int(input("Enter Length:"))
b2=int(input("Enter Breadth:"))
ob2=Rectangle()
ob2.getdata(l1,b2)
ob2.area()
ob2.perimeter()
if ob1.area()==ob2.area():
    print("Area of the Rectangles are same")
else:
    print("Area of the Rectangles are not same")
