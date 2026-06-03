from random import randint

class Moves:
    def __init__(self, name, damage_range):
        '''Attribute data types:
        name - str
        damage_range - list, [min, max]
        '''
        self.name = name
        self.damage_range = damage_range
    
    def __str__(self):
        return self.name
    
    def get_damage(self):
        return randint(self.damage_range[0], self.damage_range[1])