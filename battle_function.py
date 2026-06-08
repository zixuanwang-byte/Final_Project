# battle functions
def battle(player, enemy):
    print(f"{player.name} is battling with {enemy.name}.")
    while self.health > 0 and enemy.health > 0 :
        enemy.health -= self.attacks
        print(f"{self.name} do the attacks on {enemy.name}.")

        if enemy.health <= 0:
            print(f"{enemy.name} was loose in this battle.")
            break
        
        self.health -= enemy.attack
        print(f"{enemy.name} attacks on you.")

        if self.health <= 0:
            print(f"{self.name} was loose in this battle.")
    