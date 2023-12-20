class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def get_length(self):
        return self.length
    def get_breadth(self):
        return self.breadth
    def area(self):
        return self.get_length()*self.get_breadth()
    def __lt__(self,ob):
        if(self.area()<ob.area()):
            return "First Rectangle is Small"
        else:
            return "Second Rectangle is Small"
l1=int(input("Enter Length 1:"))
b1=int(input("Enter Breadth 1:"))
ar1=Rectangle(l1,b1)

l2=int(input("Enter Length 2:"))
b2=int(input("Enter Breadth 2:"))
ar2=Rectangle(l2,b2)

print("Area of Rectangle 1:",ar1.area())
print("Area of Rectangle 2:",ar2.area())

print(ar1<ar2)
