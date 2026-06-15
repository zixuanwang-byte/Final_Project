from character import Player, Enemy
from moves import Moves

# ---------------- MOVES ----------------
fire = Moves("Fire", [1, 5])
water = Moves("Water", [1, 5])
iron = Moves("Iron", [1, 5])
cannon = Moves("Cannon", [1, 5])
bubble = Moves("Bubble", [1, 5])

player_moves = {
    "Fire": fire,
    "Water": water,
    "Iron": iron,
    "Cannon": cannon,
    "Bubble": bubble
}

enemy_moves = [fire, water, iron, cannon, bubble]

# ---------------- CHARACTERS ----------------
Minion = Player("minion", True, 10, 10, player_moves)
Labubu = Enemy("Labubu", True, 10, 10, enemy_moves)

# ---------------- BATTLE ----------------
def battle(player, enemy):
    print(f"{player.name} is battling with {enemy.name}.")

    while player.health > 0 and enemy.health > 0:

        # Player turn
        player.use_move(enemy)

        if enemy.health <= 0:
            print(f"{enemy.name} was defeated!")
            break

        # Enemy turn
        enemy.attack(player)

        if player.health <= 0:
            print(f"{player.name} was defeated!")
            break


battle(Minion, Labubu)