from computer import *

# the ResaleShop class represents a resale shop that buys and sells computers
# I have moved the print statements from the main file to the relevant functions in order to simplify the functionality
class ResaleShop:

    # the ResaleShop object has the following attributes
    inventory : list = [] # list of computers
    name: str # name of the shop

    # the constructor creates a new ResaleShop instance and prints out the given name
    def __init__(self, name: str):
        self.name = name
        print("-" * 21)
        print(self.name)
        print("-" * 21) 

    # the buy method adds the computer to the shop inventory and returns its index
    def buy(self, computer:Computer):
            print(f"Buying {getattr(computer, "description")}")
            print("Adding to inventory...")
            new = computer
            self.inventory.append(new)
            print("Done.\n")
            return self.inventory.index(new)

    # the update_price method updates the computer's price to the given price
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            print(f"Updating price for Item ID: {item_id} to {new_price}")
            temp = self.inventory[item_id]
            temp.price = new_price
            print("Done.\n")
        else:
            print("Item", item_id, "not found. Cannot update price.") # error message if the item is not found

    # the refurbish method updates the computer's operating system as well as price based on the year of production
    def refurbish(self, item_id: int, new_os: str): 
        if self.inventory[item_id] is not None:
            print(f"Refurbishing Item ID: {item_id}, updating OS to {new_os}")
            print("Updating inventory...")
            temp = self.inventory[item_id]
            temp.update_com(new_os) # calls the update_com method from the Computer class to update the operating system
            if temp.year_made < 2000: # the price attribute is updated based on the year of production
                temp.price = 0
            elif temp.year_made < 2012:
                temp.price = 250
            elif temp.year_made < 2018:
                temp.price = 550
            else:
                temp.price = 1000
            print("Done.\n")
        else:
            print("Item", item_id, "not found. Cannot refurbish.") # error message if the item is not found

    # the sell method removes the computer from the inventory
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            print(f"Selling Item ID: {item_id}")
            self.inventory.pop(item_id)
            print(f"Item {item_id} sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.") # error message if the item is not found

    # the print_inventory method prints out the inventory
    def print_inventory(self):
        if self.inventory:
            print("Checking inventory...")
            for item in self.inventory:
                print(f"Item ID: {self.inventory.index(item)} : {item.print_com()}") # calls the print_com method from the Computer class to print out each computer's details
            print("Done.\n")
        else:
            print("No inventory to display.") # error message if the inventory is empty

