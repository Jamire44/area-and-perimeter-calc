import math as M

class Shapes:

    def circleArea(self, r):
        self.r = r

        area = M.pi * (r * r)
        print(f"The area of the circle is: {area}")

    def circlePerimeter(self, r):
        self.r = r

        per = 2 * M.pi * r
        print(f"The perimeter of the circle is: {per}")


    def squareArea(self, a):
        self.a = a

        area = a * a
        print(f"The area of the square is {area}")
        
    def squarePerimeter(self, a):
        self.a = a
        
        per = a * 4
        print(f"The perimeter of the square is {per}")

    def rectanglearea(self, l, w):
        self.l = l
        self.w = w

        area = w * l
        print(f"the area of this rectange is {area}")


    def rectanglePerimeter(self, l, w):
        self.w = w
        self.l = l

        per = 2 * (l + w)
        print(f"The perimeter of the rectangle is {per}")



shape = Shapes()


print("1. Circle")
print("2. Square")
print("3. Rectangle")

choice = input("Please choose which shape you would like to see the Area and Perimeter of : ")

if choice == "1":
    r = float(input("Please enter the radius of the circle: "))
    shape.circleArea(r)
    shape.circlePerimeter(r)
    
elif choice == "2":
    a = float(input("Please enter the length of one side in the square: "))
    shape.squareArea(a)
    shape.squarePerimeter(a)

elif choice == "3":
    l = float(input("Please enter the Length of the rectangle:"))
    w = float(input("Please enter the Width of the rectangle:"))

    shape.rectanglearea(l, w)
    shape.rectanglePerimeter(l, w)






