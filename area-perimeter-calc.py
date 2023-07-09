import math as M


# Class for all of the Area and Perimeter calculations
class Shapes:

    def circleArea(self, radius):
        self.radius = radius

        area = M.pi * (radius * radius)
        print(f"\nThe area of the circle is {area}\n")

    def circlePerimeter(self, radius):
        self.radius = radius

        perimeter = 2 * M.pi * radius
        print(f"\nThe perimeter of the circle is {perimeter}\n")


    def squareArea(self, length):
        self.length = length

        area = length * length
        print(f"\nThe area of the square is {area}\n")
        
    def squarePerimeter(self, length):
        self.length = length
        
        perimeter = length * 4
        print(f"\nThe perimeter of the square is {perimeter}\n")

    def rectanglearea(self, length, width):
        self.length = length
        self.width = width

        area = width * length
        print(f"\nThe area of this rectange is {area}\n")


    def rectanglePerimeter(self, length, width):
        self.width = width
        self.length = length

        perimeter = 2 * (length + width)
        print(f"The perimeter of the rectangle is {perimeter}\n")


# Function that has a while loop to iterate over the answer of the user, if a number isnt entered the user will be prompt to try again
def logic():
    while True :
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Exit")


        # Prompting the user to pick a shape
        choice = input("\nPlease choose which shape you would like to see the Area and Perimeter of : ")
        

        # Checks if what is entered is a digit
        if choice.isdigit():

            # If-elif-else to do what the user selects
            if choice == "1":
                radius = validate_input("\nPlease enter the radius of the circle: ")
                shape.circleArea(radius)
                shape.circlePerimeter(radius)

            elif choice == "2":
                area = validate_input("\nPlease enter the length of one side in the square: ")
                shape.squareArea(area)
                shape.squarePerimeter(area)

            elif choice == "3":
                length = validate_input("\nPlease enter the Length of the rectangle: ")
                width = validate_input("\nPlease enter the Width of the rectangle: ")
                shape.rectanglearea(length, width)
                shape.rectanglePerimeter(length, width)

            elif choice == "4":
                print("Exiting...")
                quit()

            else:
                print("\nYou have entered an invalid number\n")

        else:
            print("Number is not a digit\n")



# Function to check if the user entered a number.
# If user entered a number, Number will be allowed
# If user entered something else, They will be prompted to enter a valid number
def validate_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


shape = Shapes()

logic()


