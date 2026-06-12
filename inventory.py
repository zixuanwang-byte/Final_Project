class Inventory:
    '''A simple inventory class that holds inventory name, and a list 
    which represents items in inventory. Note: use a list of Item class 
    objects for compatibility with Shop child class of Inventory.
    '''
    def __init__(self, name):
        '''Attribute data types:
        name - str
        capacity - int
        '''
        self.name = name
        self.items = []
    
    def __str__(self):
        return self.name
    
    def view_inventory(self):
        '''Print inventory contents. If inventory is empty, print empty
        inventory message.
        '''
        if len(self.items) > 0:
            print(f"\n{self}")
            for item in self.items:
                print(f" - {item}")
        else:
            print(f"\n{self} is empty!")

    def add_item(self, item):
        '''Add an item to items list of referenced object.
        - Parameter descriptions:
        - item - any data type - item to add
        '''
        self.items.append(item)
    
    def remove_item(self, item):
        '''Remove an item from items list of referenced object.
        - Parameter descriptions:
        - item - any data type - item to remove
        '''
        self.items.remove(item)
    
    def update_inventory(self, new_items):
        '''Overwrite current inventory list with provided list.
        - Parameter descriptions:
        - items_list - list - new items to replace current items
        '''
        self.items = new_items


class Shop(Inventory):
    def __init__(self, name):
        Inventory.__init__(self, name)
    
    def __str__(self):
        return self.name
    
    def open_shop(self, shopper, items_dict):
        '''Print shop items and let player buy an item.
        - Parameter descriptions:
        - shopper - Player child class object - object to represent 
        player
        - items_dict - dictionary of item names with corresponding Item 
        class objects, for comparing user input str to existing Item 
        objects.
        '''
        while True:
            if len(self.items) <= 0:
                print(f"\n{self} is empty!")
                break
            # Print shop items and collect input.
            print("\nWhat would you like to buy?")
            shopper.view_balance()
            for item in self.items:
                print(f" - {item} ${item.price}")
            print(" - cancel")
            player_choice = input("Your choice: ").capitalize()
            # Handling input.
            if player_choice == "Cancel":
                break
            # Check if inputted string corresponds to any in-game item.
            try:
                chosen_item = items_dict[player_choice]
            except:
                # Error message for string that does not correspond to 
                # any Item object.
                print("u stoopid")
                continue
            # Check if item is in shop.
            if chosen_item in self.items:
                # Check if player has enough currency.
                if chosen_item.price <= shopper.currency:
                    # self.items.remove(chosen_item)
                    shopper.inventory.add_item(chosen_item)
                    shopper.remove_currency(chosen_item.price)
                    print(f"\nSuccessfully purchased {chosen_item}!")
                    shopper.view_balance()
                else:
                    print(f"You're too broke to buy {chosen_item} XD")
            else:
                print(f"{chosen_item} is out of stock!")