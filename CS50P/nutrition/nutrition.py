info = [
    {"apple":  "130"},
    {"avocado":  "50"},
    {"banana":  "110"},
    {"sweet cherries":  "100"},
    {"kiwifruit": "90"},
    {"pear": "100"}
]

fruta = input("Item: ").lower()

for item in info:
    if fruta in item:
        print("Calories: "+item[fruta])
        break
