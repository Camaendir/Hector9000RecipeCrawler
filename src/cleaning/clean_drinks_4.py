import json
import os.path
from src.cleaning.clean_ingredients_3 import main as cleaning_ingredients
from pathlib import Path
# clean_drinks_4.py
# deleting all faulty drinks and drinks that cant be served


def main():
    print("Cleaning up Drink from partially Cleaned Drink Data")
    if not os.path.isfile(Path("../Savefiles/drinks_C1.txt")):
        print("Corresponding Drink Data Savefiles not found. Creating one")
        cleaning_ingredients()
    Drinks = []
    with open(Path("../Savefiles/drinks_C1.txt"), "r") as f:
        items = json.loads(f.read())["items"]
        index = 0
        final_items = 0
        for item in items:
            index = index + 1
            print("Cleaning Drink Nr. %d" % index)
            ingredient_counter = 0
            faulty = False
            item["p3"] = []
            #print(item["drink_name"])
            remove = []
            for ing in item["ingredients"]:
                #print(ing)
                if ing["Purity"] is 2:
                    faulty = True
                    break
                elif ing["Purity"] is 3:
                    remove.append(ing)
                    item["p3"].append(ing)
                else:
                    ingredient_counter = ingredient_counter + 1
            for rv in remove:
                item["ingredients"].remove(rv)
            if ingredient_counter is not 0 and ingredient_counter is not 1 and faulty is False:
                Drinks.append(item)
                final_items = final_items + 1
        print("Found %d final Drinks" % final_items)
    with open(Path("../Savefiles/drinks_C2.txt"), "w+") as f:
        f.write(json.dumps({"items": Drinks},  indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
