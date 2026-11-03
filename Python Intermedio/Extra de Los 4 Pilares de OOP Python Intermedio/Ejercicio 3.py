class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"Brand: {self._brand}, Year: {self._year}"

class Car(Vehicle):
    def __init__(self, brand, year, doors, engine):
        super().__init__(brand, year)
        self.doors = doors
        self.engine = engine

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Doors: {self.doors}, Engine: {self.engine}"

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type, wheels):
        super().__init__(brand, year)
        self.type = type
        self.wheels = wheels

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