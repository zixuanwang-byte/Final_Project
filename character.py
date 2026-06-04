from random import choice
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
            print(f"\n{self} has been defeated!")
    
    def deal_damage(self, move, target):
        damage = move.get_damage()
        target.take_damage(damage)
        print(f"\n{self} uses {move} and deals {damage} damage to {target}!")


class Player(Character):
    def __init__(self, name, alive, health, max_health, moves):
        Character.__init__(self, name, alive, health, max_health, moves)
    
    def use_move(self, enemy):
        while True:
            print("\nWhich move would you like to use?")
            for move in self.moves:
                print(f" - {move}")
            player_choice = input("Your choice: ")
            if player_choice.lower() in self.moves.keys():
                chosen_move = self.moves[player_choice]
                self.deal_damage(chosen_move, enemy)
                break
            else:
                print("u stoopid")


class Enemy(Character):
    def __init__(self, name, alive, health, max_health, moves):
        Character.__init__(self, name, alive, health, max_health, moves)
        self.moves_list = list(self.moves.values())
    
    def attack(self, player):
        chosen_move = choice(self.moves_list)
        self.deal_damage(chosen_move, player)