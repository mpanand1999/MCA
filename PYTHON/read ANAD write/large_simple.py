
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        ar=self.length*self.breadth
        return ar
            
l1=int(input("Enter Length 1:"))
b1=int(input("Enter Breadth 1:"))
ar1=Rectangle(l1,b1)

l2=int(input("\nEnter Length 2:"))
b2=int(input("Enter Breadth 2:"))
ar2=Rectangle(l2,b2)

print("\nArea of Rectangle 1:",ar1.area())
print("Area of Rectangle 2:",ar2.area())

if(ar1.area()<ar2.area()):
   print("First Rectangle is Small")
else:
    print("Second Rectangle is Small")


