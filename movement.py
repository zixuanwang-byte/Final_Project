from character import Player, Enemy
from moves import Moves

'''# Test code for classes. Comment out or delete later.
move1 = Moves("test move 1", [1, 5])
move2 = Moves("test move 2", [2, 3])
test_moves_player = {"move 1": move1, "move 2": move2}
test_moves_enemy = [move1, move2]
test_char1 = Player("test char 1", True, 10, 10, test_moves_player)
test_char2 = Enemy("test char 2", True, 10, 10, test_moves_enemy)

test_char1.use_move(test_char2)
test_char2.attack(test_char1)

test_char1.view_health()
test_char2.view_health()'''


# ---------------- MOVES ----------------
fire = Moves("Fire Banana", [1, 5])
water = Moves("Water Banana", [1, 5])
iron = Moves("Iron Fail Banana", [1, 5])
cannon = Moves("Cannon Banana", [1, 5])
bubble = Moves("Bubble Banana", [1, 5])

# Player moves (dictionary required by Player class)
player_moves = {
    "Fire": fire,
    "Water": water,
    "Iron": iron,
    "Cannon": cannon,
    "Bubble": bubble
}

# Enemy moves (list required by Enemy class)
enemy_moves = [fire, water, iron, cannon, bubble]

# ---------------- CHARACTERS ----------------
Minion = Player("Minion", True, 10, 10, player_moves)
Labubu = Enemy("Labubu", True, 10, 10, enemy_moves)

# ---------------- BATTLE ATTACK MENU ----------------
minion_attacks = {
    "Bubble": "Bubble Banana",
    "Water": "Water Banana",
    "Iron": "Iron Fail Banana",
    "Fire": "Fire Banana",
    "Cannon": "Cannon Banana"
}

def battle_attacks():
    print("\nWhich Banana type would you like to use for attack?")
    for option in minion_attacks:
        print(f" - {option}")

    choice = input("Choice: ").capitalize()

    if choice in minion_attacks:
        print(f"You used {minion_attacks[choice]}!")
    else:
        print("Invalid option!")

# ---------------- MOVEMENT (FIXED) ----------------
def move(character, direction):
    if direction == "north":
        character.y += 1
    elif direction == "south":
        character.y -= 1
    elif direction == "east":
        character.x += 1
    elif direction == "west":
        character.x -= 1

    print(f"{character.name} moved {direction}.")

# ---------------- TEST ----------------
battle_attacks()

move(Minion, "north")
move(Minion, "west")