map_ = [["Zimomo's soldiers", "", "Artic Battlefeild", "", "Minions"],
    ["Zimomo's soldiers", "Zimomo", "Artic Battlefeild", "Scarlett Overkill", "Minions"],
    ["Zimomo's soldiers", "", "Artic Battlefeild", "", "Minions"]
    ]


for row in map_:
    new_list = []
    for item in row:
        new_list.append(item + " "*(18-len(item)))
    print("|".join(new_list))