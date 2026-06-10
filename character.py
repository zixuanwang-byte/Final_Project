from random import choice


class Character:
    '''A simple character class that holds basic character stats, and 
    methods to view health, take damage, and heal.
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
        self.y = 0
        self.x = 0
    
    def __str__(self):
        return self.name
    
    def view_health(self):
        '''Print current health value of referenced object.'''
        print(f"{self} is a at {self.health} health!")

    def take_damage(self, damage):
        '''Take damage, aka decrease health value of referenced object.
        - Parameter descriptions:
        damage - int - amount of health to remove
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
        heal_amount - int - amount of health to add
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
            player_choice = input("Your choice: ")
            if player_choice.lower() in self.moves.keys():
                chosen_move = self.moves[player_choice]
                damage_dealt = chosen_move.get_damage()
                target.take_damage(damage_dealt)
                print(f"\nYou use {chosen_move} and deals {damage_dealt} damage "
                      + f"to {target}!")
                break
            else:
                print("u stoopid")


class Enemy(Character):
    '''Character child class with added moves attribute, and attack 
    method which chooses a random move to use.
    '''
    def __init__(self, name, alive, health, max_health, moves):
        Character.__init__(self, name, alive, health, max_health)
        '''Attribute data types:
        moves - list of Moves objects
        '''
        self.moves = moves
    
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