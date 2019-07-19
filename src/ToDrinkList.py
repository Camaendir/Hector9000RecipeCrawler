import json
import os.path
from src.cleaning.clean_json_5 import main as clean_json
from pathlib import Path
# ToDrinkList.py


def get_Drinks():
    print("Loading Drinks from Drink Safefile")
    if not os.path.isfile(Path("Savefiles/Drinks.drk")):
        print("Drinks Savefiles not found. Creating one.")
        clean_json()
    DrinkList = []
    with open(Path("../Savefiles/Drinks.drk"), "r") as f:
        items = json.loads(f.read())["Drinks"]
        for item in items:
            Drink = {}
            Drink["color"] = item["color"]
            Drink["name"] = item["name"]
            Drink["recipe"] = []
            for ing in item["recipe"]:
                Drink["recipe"].append(("ingr", ing["name"], ing["amt"]))
            DrinkList.append(Drink)
        return DrinkList


if __name__ == "__main__":
    get_Drinks()
