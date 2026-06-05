from random import randint

class Moves:
    '''Simple attack move class, containing attack name and damage 
    value range. Actual damage dealt is chosen randomly from said
    range.
    '''
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
        '''Calculate the damage this move will inflict in one attack by
        getting a random integer in range of the damage_range attribute.
        '''
        return randint(self.damage_range[0], self.damage_range[1])