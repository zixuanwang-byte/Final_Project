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

#story line for version 1
#Stroy of version 2.0 
def story_lines1():
    print("This game's name is Labubu and Minion War Battle.")
    print("This story is about the war between the minions and Labubus.")
    print("One minion's name was Kevin, he decided to go"
          + " to New York city to find the baddest villain in the world to save"
          + " his people.")
    print("")
    choice = input("Do you want to continue to read the story? (yes/no): ")
    if choice.lower() == "yes":
        print()
        print("Kevin took Stuart and Bob with him. They found their boss, she is"
              + " the worlds top female supervillain named Scarlett Overkill."
              + " They send the message tp their family."
              + " The whole minion group goes to the"
              + " city to see their new boss.")
    print()    
    choice = input("Do you want to still continue to read the story? (yes/no): ")
    if choice.lower() == "yes": 
        print()    
        print("When minions leave for New York city."
            + " Labubus king, whose name is Zimomo, wants to make his kingdom big."
            + " He is an enemy of minions but minions do not let Labubus take over "
            + " their ice cave. He gave command to his soldiers to attack on"
            + " home. When the minions figured out that Zimomo took"
            + " over their house."
            + "Minion came back with their new boss to fight with Labubus.")

def view_map():
    map_ = [["Zimomo's soldiers", "", "Artic Battlefeild", "", "Minions"],
        ["Zimomo's soldiers", "Zimomo", "Artic Battlefeild", "Scarlett Overkill", "Minions"],
        ["Zimomo's soldiers", "", "Artic Battlefeild", "", "Minions"]
        ]


    for row in map_:
        new_list = []
        for item in row:
            new_list.append(item + " "*(18-len(item)))
        print("|".join(new_list))

def battle(player, enemy):
    print(f"{player.name} is battling with {enemy.name}.")

    while player.health > 0 and enemy.health > 0:

        # Player turn
        player.use_move(enemy)

        if enemy.health <= 0:
            print("Minions are going to take their"
                  + " home back from if they win, else"
                   + " they are going to live with their boss.")
            break

        # Enemy turn
        enemy.attack(player)

        if player.health <= 0:
            print(" Labubu lose they are going to"
                  + " leave the minion's house, else they are going"
                  + " to live in the cave.")
            break

        input("ENTER to continue")


story_lines1()
view_map()
input("\nENTER to battle")
battle(Minion, Labubu)