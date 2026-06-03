# Idk if this works.

from moves import Moves

class Character:
    def __init__(self, name, alive, health, max_health, moves):
        '''Attribute data types:
        name - str
        alive - bool
        health - int
        max_health - int
        moves - dictionary of move names with corresponding Moves objects
        '''
        self.name = name
        self.alive = alive
        self.health = health
        self.max_health = max_health
        self.moves = moves
    
    def __str__(self):
        return self.name
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"{self} has been defeated!")
    
    def deal_damage(self, damage, target):
        target.take_damage(damage)
        print(f"{self} deals {damage} damage to {target}!")

    def use_move(self, enemy):
        print("\nWhich move would you like to use?")
        for move in self.moves:
            print(f" - {move}")
        chosen_move = input("Your choice: ")
        if chosen_move in self.moves.items():
            damage_dealt = chosen_move.get_damage()
            self.deal_damage(damage_dealt, enemy)
        pass