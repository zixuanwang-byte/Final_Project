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

attacks = {
    minion_banana :[
        "Fire Banana", 
        "Water Banana", 
        "Iron Fail Banana", 
        "Cannon Banana", 
        "Bubble Banana"],
    
    Labubu_ball : [
        "Bubble ball",
        "Iron Fail ball", 
        "Cannon ball", 
        "Fire ball", 
        "Water ball"]}

Labubu_attacks = {"Fire": Fire ball, "Bubble": Bubble ball, "Iron": Iron Fail ball,
                 "Cannon": Cannon ball, "Water": Water ball}
minion_attacks = {"Bubble": Bubble Banana, "Water": Water Banana, "Iron": Iron Fail Banana,
                 "Fire": Fire Banana, "Cannon": Cannon Banana}

def battle_atttacks():
    print("\n Which Banana type you like to use for attack?")
    for option in minion_attacks:
        print(f" - {option}")
    choice = input("choice: ")
    if choice in minion_attacks:
        minion_attacks[choice]()
    else:
        print("Sorry this option is not valid. Please try again.")
print(battle_attacks)

def move(self, direction):
    if direction == "north":
        self.x += 1
    elif direction == "east":
        self.x -= 1
    elif direction == "south":
        self.y += 1
    elif direction == "west":
        self.y -= 1
    
    print(f"{self.name} moved to the {direction}.")

player = Character("Minion")

player.move("north")
player.move("west")