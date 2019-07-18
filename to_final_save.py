import json
import math

# to_final_save.py

def main():
    Drinks = []
    before = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "orange juice", "grenadine", "mate")
    after = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "oj", "gren", "mate" )
    with open("ingredients_sorted_clean.txt", "r") as f:
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
                Drink["recipe"].append({"name": after[before.index(ing["ing_name"])],"amt": int(float(ing["ing_ammount"]) * multiplicator)})
            Drinks.append(Drink)
    with open("Drinks.txt", "w+") as f:
        f.write(json.dumps({"Drinks": Drinks}, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()



# name, color, recipe -> ("ingr", %NAME%, %AMMOUNT%)