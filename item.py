class Item:
    ''' A basic Item class that holds item stats. '''
    def __init__(self, name, effect, effect_quantity, price):
        '''Attribute data types:
        name - str
        effect - str
        effect_quantity - int
        price - int
        '''
        self.name = name
        self.effect = effect
        self.effect_quantity = effect_quantity
        self.price = price
    
    def __str__(self):
        return self.name