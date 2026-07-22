class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = 0

    def add_passengers(self, passengers):
        if self.passengers + passengers <= self.max_passengers:
            self.passengers += passengers
        else:
            print("The bus is full")

    def remove_passengers(self, passengers):
        if self.passengers - passengers >= 0:
            self.passengers -= passengers
        else:
            print("There are no passengers to remove")

    def get_passengers(self):
        return self.passengers

def main():
    print("Bus Control System\n")
    max_passengers = int(input("Insert the maximum number of passengers: "))
    bus = Bus(max_passengers)

    while True:
        print("\n1. Add passengers")
        print("2. Remove passengers")
        print("3. Get passengers")
        print("4. Exit")

        option = int(input("Insert an option: "))

        if option == 1:
            passengers = int(input("Insert the number of passengers to add: "))
            bus.add_passengers(passengers)
        elif option == 2:
            passengers = int(input("Insert the number of passengers to remove: "))
            bus.remove_passengers(passengers)
        elif option == 3:
            print(f"The number of passengers in the bus is: {bus.get_passengers()}")
        elif option == 4:
            print("Goodbye")
            break
        else:
            print("Invalid option")
main()