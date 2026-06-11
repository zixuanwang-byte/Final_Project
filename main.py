from character import Player, Enemy
from moves import Moves
from inventory import Shop
from item import Item

# Test code for classes. Comment out or delete later.
move1 = Moves("Move 1", [1, 5])
move2 = Moves("Move 2", [2, 3])
test_moves_player = {"Test Move 1": move1, "Test Move 2": move2}
test_moves_enemy = [move1, move2]
test_player = Player("Player", True, 10, 10, test_moves_player)
test_enemy = Enemy("Enemy", True, 10, 10, test_moves_enemy, 4)

random_list = ["BTP", "cookie", "Labubu"]

item1 = Item("Item 1", "<FX>", "<FX Quantity>", 35)
item2 = Item("Item 2", "<FX>", "<FX Quantity>", 10)
test_items = {"Test Item 1": item1, "Test Item 2": item2}
shop_items = [item1, item2]
test_player.update_currency(40)

shop = Shop("Shop")
shop.update_inventory(shop_items)

shop.open_shop(test_player, test_items)