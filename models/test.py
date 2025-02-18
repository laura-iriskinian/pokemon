import json

with open("models/pokedex.json", "r", encoding = "utf-8") as file:
    pokedex = json.load(file)
player_name = ""
for data in pokedex:
            for player in data["players"]:
                print(type(data))
                    
