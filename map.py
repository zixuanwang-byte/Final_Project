from tabulate import tabulate

map = [["Zimomo's soldiers", "", "Artic Battlefeild", "", "Minions"],
    ["Zimomo's soldiers", "Zimomo", "Artic Battlefeild", "Scarlett Overkill", "Minions"],
    ["Zimomo's soldiers", "", "Artic Battlefeild", "", "Minions"]]
headers = ["  West", "", "  Center","", "  East"]

print(tabulate(map, headers=headers, tablefmt="fancy_grid"))

