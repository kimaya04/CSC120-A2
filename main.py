# Import a few useful containers from the typing module
from typing import Dict, Union

# Import the functions from oo_resale_shop.py and computer.py
from computer import *
from oo_resale_shop import *

def main():

    # First we need to create a resale shop
    shop = ResaleShop("COMPUTER RESALE STORE")

    # Now let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Add it to the resale store's inventory
    computer_id = shop.buy(computer)

    # Make sure it worked by checking inventory
    shop.print_inventory()

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    shop.refurbish(computer_id, new_OS)

    # Make sure it worked by checking inventory
    shop.print_inventory()

    # Now, let's update the price
    new_price = 2000
    shop.update_price(computer_id, new_price)

    # Make sure it worked by checking inventory
    shop.print_inventory()
    
    # Now, let's sell it!
    shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    shop.print_inventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()
