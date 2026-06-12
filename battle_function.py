from character import Player, Enemy 
from Player import use_move
from Enemy import attack 

Minion = Player("minion", True, 10, 10)
Labubu = Enemy("Labubu", True, 10, 10)


# battle functions
def battle(player, enemy):
    attack = 1

    print(f"{player.name} is battling with {enemy.name}.")

    while player.health > 0 and enemy.health > 0 :
        #enemy.health -= player.attack
        player.use_move(enemy)
        print(f"{player.name} do the attacks on {enemy.name}.")

        if enemy.health <= 0:
            print(f"{enemy.name} was loose in this battle.")
            break
        
        #player.health -= enemy.attack
        enemy.attack(player)
        print(f"{enemy.name} attacks on you.")

        if player.health <= 0:
            print(f"{player.name} was loose in this battle!")
            break 

battle(Minion, Labubu)