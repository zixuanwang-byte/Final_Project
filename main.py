from character import Player, Enemy
from moves import Moves

# Test code for classes. Comment out or delete later.
move1 = Moves("Move 1", [1, 5])
move2 = Moves("Move 2", [2, 3])
test_moves_player = {"move 1": move1, "move 2": move2}
test_moves_enemy = [move1, move2]
test_player = Player("Player", True, 10, 10, test_moves_player)
test_enemy = Enemy("Enemy", True, 10, 10, test_moves_enemy, 4)

random_list = ["BTP", "cookie", "Labubu"]
