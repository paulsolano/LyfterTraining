class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

radius = float(input("Insert the radius of the circle: "))
circle = Circle(radius)
print("Area of the circle:", circle.get_area())
