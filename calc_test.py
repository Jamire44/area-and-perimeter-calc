import unittest
from unittest.mock import patch
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
        return area

    def calculate_perimeter(self):
        perimeter = 2 * M.pi * self.radius
        return perimeter
    
class Square(Shapes):

    def __init__(self, length):
        self.length = length
        

    def calculate_area(self):
        area = self.length * self.length
        return area

    def calculate_perimeter(self):
        self.length = self.length
        
        perimeter = self.length * 4
        return perimeter

class Rectangle(Shapes):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.width * self.length
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

# Testing Shapes 

class TestShapes(unittest.TestCase):

    class MockShape(Shapes):
        def calculate_area(self):
            return 10
        
        def calculate_perimeter(self):
            return 20
        
    def test_calculate_area(self):
        shape = self.MockShape()
        result = shape.calculate_area()
        self.assertEqual(result, 10)

    def test_calculate_perimeter(self):
        shape = self.MockShape()
        result = shape.calculate_perimeter()
        self.assertEqual(result, 20)

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_area(), M.pi * (5 * 5))

    def test_circle_perimeter(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.calculate_perimeter(), 2 * M.pi * 5)

    def test_square_area(self):
        square = Square(9)
        self.assertAlmostEqual(square.calculate_area(), 9 * 9)

    def test_square_perimeter(self):
        square = Square(4)
        self.assertAlmostEqual(square.calculate_perimeter(), 4 * 4)

    def test_rectangle_area(self):
        rectangle = Rectangle(6,1112)
        self.assertAlmostEqual(rectangle.calculate_area(), 6 * 1112)

    def test_rectangle_perimeter(self):
        rectangle = Rectangle(6, 9)
        self.assertAlmostEqual(rectangle.calculate_perimeter(), 2 * (6 + 9))

def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


class TestValidateInput(unittest.TestCase):
    def test_valid_input(self):
        prompt = "Enter a number: "
        user_input = "123"
        expected_output = 123

        with patch('builtins.input', return_value = user_input):
            actual_output = validate_input(prompt)

            self.assertEqual(actual_output, expected_output)
         

if __name__ == '__main__':
    unittest.main()
