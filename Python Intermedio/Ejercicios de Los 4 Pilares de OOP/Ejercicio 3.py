class Flier:
    def fly(self):
        print("The duck is flying")

class Swimmer:
    def swim(self):
        print("The duck is swimming")

class Duck(Flier, Swimmer):
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"The duck's name is: {self.name}")

def main():
    duck = Duck("Donald")
    duck.display_name()
    duck.fly()
    duck.swim()

main()
