import json

# ToDrinkList.py

def get_Drinks():
    DrinkList = []
    with open("Drinks.txt", "r") as f:
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