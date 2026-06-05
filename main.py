from character import Player, Enemy
from moves import Moves

# Test code for classes. Comment out or delete later.
move1 = Moves("test move 1", [1, 5])
move2 = Moves("test move 2", [2, 3])
test_moves_player = {"move 1": move1, "move 2": move2}
test_moves_enemy = [move1, move2]
test_char1 = Player("test char 1", True, 10, 10, test_moves_player)
test_char2 = Enemy("test char 2", True, 10, 10, test_moves_enemy)

test_char1.use_move(test_char2)
test_char2.attack(test_char1)