#Write lambda functions to find the area of a square, rectangle, and triangle


square_area = lambda a: a**2
rectangle_area = lambda l, b: l * b
triangle_area = lambda ba, h: 0.5 * ba * h


a = int(input("\nEnter the length: "))
print("Area of the square:", square_area(a))

l = int(input("\nEnter the length: "))
b = int(input("Enter the breadth: "))
print("Area of the rectangle:", rectangle_area(l, b))


ba = int(input("\nEnter the base: "))
h = int(input("Enter the height: "))
print("Area of the triangle:", triangle_area(ba, h))
