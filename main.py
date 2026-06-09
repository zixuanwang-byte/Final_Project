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

# test_player.use_move(test_enemy)
# test_enemy.attack(test_player)

# test_player.inventory.add_item("random item")
test_player.inventory.view_inventory()
test_player.inventory.update_inventory(random_list)
test_player.inventory.view_inventory()

test_player.add_currency(5)
print(test_player.currency)

test_player.remove_currency(7)
print(test_player.currency)

test_player.add_currency(13)
test_player.update_currency(25)
print(test_player.currency)