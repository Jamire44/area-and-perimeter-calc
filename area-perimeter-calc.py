import unittest
import math as M

# Class for all of the Area and Perimeter calculations

class Shapes:
    def calculate_area(self):
        pass

    def calculate_perimeter(Self):
        pass

class Circle(Shapes):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = M.pi * (self.radius * self.radius)
        print(f"\nThe area of the circle is {area}\n")

    def calculate_perimeter(self):
        perimeter = 2 * M.pi * self.radius
        print(f"\nThe perimeter of the circle is {perimeter}\n")

class Square(Shapes):

    def __init__(self, length):
        self.length = length
        

    def calculate_area(self):
        area = self.length * self.length
        print(f"\nThe area of the square is {area}\n")
        
    def calculate_perimeter(self):
        self.length = self.length
        
        perimeter = self.length * 4
        print(f"\nThe perimeter of the square is {perimeter}\n")

class Rectangle(Shapes):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.width * self.length
        print(f"\nThe area of this rectange is {area}\n")


    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print(f"The perimeter of the rectangle is {perimeter}\n")