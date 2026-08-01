from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def calculate_area(self):
            return 3.14 * self.radius ** 2

        def calculate_perimeter(self):
            return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side):
            self.side = side

    def calculate_area(self):
            return self.side ** 2

    def calculate_perimeter(self):
            return 4 * self.side

class Rectangle(Shape):
    def __init__(self, width, height):
            self.width = width
            self.height = height

    def calculate_area(self):
            return self.width * self.height

    def calculate_perimeter(self):
            return 2 * (self.width + self.height)

def main():
    circle = Circle(radius=8)
    rectangle = Rectangle(width=7, height=13)
    square = Square(side=8)

    print(f"Circle Area: {circle.calculate_area()}")
    print(f"Circle Perimeter: {circle.calculate_perimeter()}")

    print(f"Rectangle Area: {rectangle.calculate_area()}")
    print(f"Rectangle Perimeter: {rectangle.calculate_perimeter()}")

    print(f"Square Area: {square.calculate_area()}")
    print(f"Square Perimeter: {square.calculate_perimeter()}")

if __name__ == "__main__":
    main()