import json
import os.path
from src.crawling.get_drink_2 import main as get_drinks
# clean_ingredients_3.py
# cleaning up strings and sorting the ingredients more


def main():
    print("Cleaning Ingredients from raw Drink Data")
    if not os.path.isfile("../Savefiles/drinks_raw_full.txt"):
        print("Could not find raw Drink data. Gathering Drink data. This may take a while (ca. 10-15 minutes)" +
              " and will stress your internet connection")
        get_drinks()
    amt_def = [(10, "a small splash", "a splash", "splash")]
    text = open("../Savefiles/drinks_raw_full.txt", "r").read()
    items = json.loads(text)["items"]
    index = 0
    not_found_list = []
    definitions = []
    for item in items:
        index = index + 1
        print("Cleaning Ingredient from Drink Nr. %d" % index)
        for ing in item["ingredients"]:
            if ing["Purity"] == 3:
                Found = False
                for defi in amt_def:
                    first = True
                    for exp in defi:
                        if first:
                            first = False
                            continue
                        if exp in ing["body"]:
                            ing["ing_ammount"] = defi[0]
                            ing["ing_name"] = ing["body"].replace(exp, "").strip()
                            not_found_list.append(ing["ing_name"])
                            ing["Purity"] = 2
                            Found = True
                            break
                    if Found:
                        break
                if not Found:
                    del ing
            elif ing["Purity"] == 2:
                Found = False
                for defi in amt_def:
                    first = True
                    for exp in defi:
                        if first:
                            first = False
                            continue
                        if exp in ing["body"]:
                            ing["ing_ammount"] = defi[0]
                            ing["Purity"] = 1
                            Found = True
                            break
                    if Found:
                        break
                if not Found:
                    definitions.append(ing["body"])
                    ing["Purity"] = 3
            elif ing["Purity"] == 1:
                ing["ing_ammount"] = calculate_ammount(ing["ing_ammount"])
                loc_name = check_parity(ing["ing_name"])
                if loc_name is ing["ing_name"]:
                    not_found_list.append(ing["ing_name"])
                    ing["Purity"] = 2
                else:
                    ing["ing_name"] = loc_name
            else:
                print("Something went wrong! Body: %s" % ing["body"])
    with open("../Savefiles/drinks_C1.txt", "w+") as f:
        f.write(json.dumps({"items": items},  indent=4, sort_keys=True))
    with open("../Savefiles/not_found.txt", "w+") as f:
        f.write(json.dumps(not_found_list,  indent=4, sort_keys=True))
    with open("../Savefiles/definition.txt", "w+") as f:
        f.write(json.dumps(definitions, indent=4, sort_keys=True))
    print("Cleaned Ingredients from %d Drinks" % index)


def calculate_ammount(ammout_str):
    ammout_str = ammout_str.replace("ml", "")
    ammout_str = ammout_str.replace(" ", "").replace("`", "")
    pos = ammout_str.find('/')
    if pos is not -1:
        teiler = ammout_str[pos + 1]
        ammout_str = ammout_str.replace("1/" + teiler, "").replace("/" +teiler, "")
        return str(float(ammout_str) + (float(1) / float(teiler)))
    return ammout_str


def check_parity(ingredient):
    ingredients = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "orange juice", "grenadine", "mate", "cola")
    for ing in ingredients:
        if ing in ingredient.lower():
            return ing
    return ingredient


if __name__ == "__main__":
    main()
