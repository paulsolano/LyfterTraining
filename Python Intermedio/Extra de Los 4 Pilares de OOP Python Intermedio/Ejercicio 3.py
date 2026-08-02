class Vehicle:
    def __init__(self, _brand, _year):
        self._brand = _brand
        self._year = _year

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}"

class Car(Vehicle):
    def __init__(self, _brand, _year, _doors, _engine):
        super().__init__(_brand, _year)
        self.doors = _doors
        self.engine = _engine

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Doors: {self.doors}, Engine: {self.engine}"

class Motorcycle(Vehicle):
    def __init__(self, _brand, _year, _type, _wheels):
        super().__init__(_brand, _year)
        self.type = _type
        self.wheels = _wheels

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Type: {self.type}, Wheels: {self.wheels}"

def main():
    vehicle1 = Car("Toyota", 2020, 4, "Gasoline")
    vehicle2 = Motorcycle("Yamaha", 2022, "Deportiva", 2)

    print(vehicle1.get_info())
    print(vehicle2.get_info())

if __name__ == "__main__":
    main()