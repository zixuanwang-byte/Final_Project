from random import choice
from inventory import Inventory


class Character:
    '''A simple character class that holds basic character stats, and 
    method to take damage.
    '''
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
        '''Take damage, aka decrease health value of referenced object.
        - Parameter descriptions:
        - damage - int - amount of health to remove
        '''
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False
            print(f"\n{self} has been defeated!")

    def heal(self, heal_amount):
        '''Increace health of referenced object. Health value cannot 
        exceed value of max_health attribute.
        - Parameter descriptions:
        - heal_amount - int - amount of health to add
        '''
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health


class Player(Character):
    '''Character child class with added moves attribute, and 
    use_moves() method which allows user to choose a move to use.
    '''
    def __init__(self, name, alive, health, max_health, moves):
        Character.__init__(self, name, alive, health, max_health)
        '''Attribute data types:
        moves - dictionary of move names with corresponding Moves objects
        '''
        self.moves = moves
        self.inventory = Inventory(f"{self}'s Inventory")
        self.currency = 0

    
    def use_move(self, target):
        '''Ask user to choose from moves contained in moves attribute, 
        calculate damage value by calling chosen move's get_damage() 
        method, then deal said amount of damage to target by calling 
        target object's take_damage() method.
        - Parameter descriptions:
        - target - Character class or child of said class - target to 
        inflict damage onto
        '''
        while True:
            # Repeatedly prompt for input if user does not provide 
            # valid input.
            print("\nWhich move would you like to use?")
            for move in self.moves:
                print(f" - {move}")
            player_choice = input("Your choice: ").capitalize()
            if player_choice in self.moves.keys():
                chosen_move = self.moves[player_choice]
                damage_dealt = chosen_move.get_damage()
                target.take_damage(damage_dealt)
                print(f"\nYou use {chosen_move} and deal {damage_dealt} damage "
                      + f"to {target}!")
                break
            else:
                print("u stoopid")
    
    def add_currency(self, amount):
        '''Increase currency value of referenced object.
        - Parameter descriptions:
        - amount - int - amount of currency to add
        '''
        self.currency += amount
    
    def remove_currency(self, amount):
        '''Decrease currency value of referenced object. Currency value
        cannot be less than 0.
        - Parameter descriptions:
        - amount - int - amount of currency to remove
        '''
        self.currency -= amount
        if self.currency < 0:
            self.currency = 0
    
    def update_currency(self, amount):
        '''Overwrite currency value of referenced object with provided 
        value.
        - Parameter descriptions:
        - amount - int - new value to replace current value
        '''
        self.currency = amount
    
    def view_balance(self):
        ''' Print player's currency value. '''
        print(f"Your balance: ${self.currency}")


class Enemy(Character):
    '''Character child class with added moves attribute, and attack 
    method which chooses a random move to use.
    '''
    def __init__(self, name, alive, health, max_health, moves, loot_amount):
        Character.__init__(self, name, alive, health, max_health)
        '''Attribute data types:
        moves - list of Moves objects
        loot_amount - int
        '''
        self.moves = moves
        self.loot_amount = loot_amount
    
    def attack(self, target):
        '''Choose a random move from moves listed in moves attribute, 
        use Move class' get_damage() method to return a damage value, 
        then deal said amount of damage to target by calling target 
        object's take_damage() method.
        - Parameter descriptions:
        - target - Character class or child of said class - target to 
        inflict damage onto
        '''
        chosen_move = choice(self.moves)
        damage_dealt = chosen_move.get_damage()
        target.take_damage(damage_dealt)
        print(f"\n{self} attacks you with {chosen_move} and deals "
              + f"{damage_dealt} damage!")