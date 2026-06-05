from random import choice


class Character:
    def __init__(self, name, alive, health, max_health):
        '''Attribute data types:
        name - str
        alive - bool
        health - int
        max_health - int
        '''
        self.name = name
        self.alive = alive
        self.health = health
        self.max_health = max_health
    
    def __str__(self):
        return self.name
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"\n{self} has been defeated!")
    
    def deal_damage(self, damage, target):
        target.take_damage(damage)


class Player(Character):
    def __init__(self, name, alive, health, max_health, moves):
        Character.__init__(self, name, alive, health, max_health)
        '''Attribute data types:
        moves - dictionary of move names with corresponding Moves objects
        '''
        self.moves = moves

    
    def use_move(self, enemy):
        while True:
            print("\nWhich move would you like to use?")
            for move in self.moves:
                print(f" - {move}")
            player_choice = input("Your choice: ")
            if player_choice.lower() in self.moves.keys():
                chosen_move = self.moves[player_choice]
                damage_dealt = chosen_move.get_damage()
                self.deal_damage(damage_dealt, enemy)
                print(f"\nYou use {chosen_move} and deals {damage_dealt} damage "
                      + f"to {enemy}!")
                break
            else:
                print("u stoopid")


class Enemy(Character):
    def __init__(self, name, alive, health, max_health, moves):
        Character.__init__(self, name, alive, health, max_health)
        '''Attribute data types:
        moves - list of Moves objects
        '''
        self.moves = moves
    
    def attack(self, attack_target):
        chosen_move = choice(self.moves)
        damage_dealt = chosen_move.get_damage()
        self.deal_damage(damage_dealt, attack_target)
        print(f"\n{self} attacks you with {chosen_move} and deals "
              + f"{damage_dealt} damage!")