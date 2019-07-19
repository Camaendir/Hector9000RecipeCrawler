import json
import math
import os.path
from src.cleaning.clean_drinks_4 import main as clean_drinks
from pathlib import Path
# clean_json_5.py


def main():
    print("Cleaning json from cleaned Drink Data")
    if not os.path.isfile(Path("../Savefiles/drinks_C2.txt")):
        print("Cleaned Drinks Savefiles not found. Creating one")
        clean_drinks()
    Drinks = []
    before = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "orange juice", "grenadine", "mate", "cola")
    after = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "oj", "gren", "mate", "coke")
    with open(Path("../Savefiles/drinks_C2.txt"), "r") as f:
        items = json.loads(f.read())["items"]
        for item in items:
            Drink = {}
            print(item["drink_name"])
            Drink['name'] = item["drink_name"].strip()
            Drink['color'] = "black"
            full_ammount = 0
            for ing in item["ingredients"]:
                full_ammount = full_ammount + int(math.ceil(float(ing["ing_ammount"])))
            multiplicator = float(200) / float(full_ammount)
            Drink["recipe"] = []
            for ing in item["ingredients"]:
                Drink["recipe"].append({"name": after[before.index(ing["ing_name"])], "amt": int(float(ing["ing_ammount"]) * multiplicator)})
            Drinks.append(Drink)
    with open(Path("../Savefiles/Drinks.drk"), "w+") as f:
        f.write(json.dumps({"Drinks": Drinks}, indent=4, sort_keys=True))
    print("Cleaned JSON from cleaned Drink Data")


if __name__ == "__main__":
    main()
