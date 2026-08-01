class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class Inventory: 
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
        else:
            print("The product is not in the inventory")

    def show_inventory(self):
        for product in self.products:
            print(product)

    def inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value

def main():
    print("Inventory Management System\n")
    inventory = Inventory()

    while True:
        print("1. Add product")
        print("2. Remove product")
        print("3. Show inventory")
        print("4. Show inventory value")
        print("5. Exit")

        option = int(input("Insert an option: "))

        if option == 1:
            name = input("Insert the product name: ")
            price = float(input("Insert the product price: "))
            quantity = int(input("Insert the product quantity: "))
            product = Product(name, price, quantity)
            inventory.add_product(product)
        elif option == 2:
            name = input("Insert the product name to remove: ")
            product_to_remove = None
            for product in inventory.products:
                if product.name == name:
                    product_to_remove = product
                    break
            if product_to_remove:
                inventory.remove_product(product_to_remove)
            else:
                print("The product is not in the inventory")
        elif option == 3:
            inventory.show_inventory()
        elif option == 4:
            print(f"The total value of the inventory is: {inventory.inventory_value()}")
        elif option == 5:
            print("Goodbye")
            break
        else:
            print("Invalid option")

main()