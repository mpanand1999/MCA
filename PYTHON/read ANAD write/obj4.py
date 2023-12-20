
class Rectangle:
    def getdata(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        print("Area:",ar)
    def perimeter(self):
        per=2*(self.length+self.breadth)
        print("Perimeter:",per)
#main
ch=0
l=int(input("Enter Length:"))
b=int(input("Enter Breadth:"))
ob=Rectangle()
ob.getdata(l,b)


while ch!=3:
    print("1. area")
    print("2.perimeter")
    print("3. exit")
    ch=int(input("enter your choice"))
    if ch==1:
        ob.area()
    if ch==2:
        ob.perimeter()
    else:
        print("exit")
           
 
