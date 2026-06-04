import character
from moves import Moves

move1 = Moves("test move 1", [1, 5])
move2 = Moves("test move 2", [2, 3])
test_moves = {"move 1": move1, "move 2": move2}
test_char1 = character.Player("test char 1", True, 10, 10, test_moves)
test_char2 = character.Enemy("test char 2", True, 10, 10, test_moves)

test_char1.use_move(test_char2)
test_char2.attack(test_char1)