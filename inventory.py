class Inventory:
    '''A simple inventory class that holds inventory name, inventory 
    capacity, and a list which represents items in inventory.
    '''
    def __init__(self, name, capacity):
        '''Attribute data types:
        name - str
        capacity - int
        '''
        self.name = name
        self.capacity = capacity
        self.items = []
    
    def __str__(self):
        return self.name
    
    def view_inventory(self):
        '''Print inventory contents. If inventory is empty, print empty
        inventory message.
        '''
        if len(self.items) > 0:
            print(self)
            for item in self.items:
                print(f" - {item}")
        else:
            print(f"{self} is empty!")

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