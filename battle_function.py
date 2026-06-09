from character import Player, Enemy 
from moves import Move
from character import Player, Enemy

Minion = Player("minion", True, 10, 10, 1)
Labubu = Enemy("Labubu", True, 10, 10, 1)


# battle functions
def battle(self, Player, Enemy):
    print(f"{Player.name} is battling with {Enemy.name}.")
    while self.health > 0 and Enemy.health > 0 :
        Enemy.health -= self.attack
        print(f"{self.name} do the attacks on {Enemy.name}.")

        if Enemy.health <= 0:
            print(f"{Enemy.name} was loose in this battle.")
            break
        
        self.health -= Enemy.attack
        print(f"{Enemy.name} attacks on you.")

        if self.health <= 0:
            print(f"{self.name} was loose in this battle.")

battle(Player, Minion, Labubu)