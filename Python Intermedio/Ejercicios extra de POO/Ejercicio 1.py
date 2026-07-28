class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

def main():
    print("Rectangle Area and Perimeter Calculator\n")

    while True:
        width = float(input("Insert the width of the rectangle: "))
        if width > 0:
            break
        print("Width must be a positive number.")

    while True:
        height = float(input("Insert the height of the rectangle: "))
        if height > 0:
            break
        print("Height must be a positive number.")

    rectangle = Rectangle(width, height)

    print(f"The area of the rectangle is: {rectangle.get_area()}")
    print(f"The perimeter of the rectangle is: {rectangle.get_perimeter()}")

main()