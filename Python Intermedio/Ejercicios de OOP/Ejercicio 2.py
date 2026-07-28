class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
        else:
            print("The bus is full")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
        else:
            print("That passenger is not on the bus")

    def get_passengers(self):
        return len(self.passengers)

def main():
    print("Bus Control System\n")
    max_passengers = int(input("Insert the maximum number of passengers: "))
    bus = Bus(max_passengers)
    passenger_count = 0

    while True:
        print("\n1. Add passengers")
        print("2. Remove passengers")
        print("3. Get passengers")
        print("4. Exit")

        option = int(input("Insert an option: "))

        if option == 1:
            passenger_count += 1
            person = Person(f"Passenger {passenger_count}")
            bus.add_passenger(person)
        elif option == 2:
            if bus.passengers:
                bus.remove_passenger(bus.passengers[-1])
            else:
                print("There are no passengers to remove")
        elif option == 3:
            print(f"The number of passengers in the bus is: {bus.get_passengers()}")
        elif option == 4:
            print("Goodbye")
            break
        else:
            print("Invalid option")
main()