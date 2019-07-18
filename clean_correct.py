import json

# clean_correct.py

def main():
    Drinks = []
    with open("ingredients_sorted_correct.txt", "r") as f:
        items = json.loads(f.read())
        index = 1
        final_items = 0
        for item in items:
            print("Cleaning Correctly Drink Nr. %d" % index)
            index = index + 1
            del item["faulty"]
            ingredient_counter = len(item["ingredients"])
            if ingredient_counter is not 0 and ingredient_counter is not 1:
                Drinks.append(item)
                final_items = final_items + 1
        print("Found %d final Drinks" % final_items)
    with open("ingredients_sorted_clean.txt", "w+") as f:
        f.write(json.dumps({"items": Drinks},  indent=4, sort_keys=True))
        print("Saved file")


if __name__ == "__main__":
    main()