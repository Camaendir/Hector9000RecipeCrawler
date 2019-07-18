import json

# clean.py


def main():
    text = open("ingredients_raw.txt", "r").read()
    items = json.loads(text)["items"]
    index = 0
    not_found_list = []
    for item in items:
        index = index + 1
        print("Cleaning Drink Nr. %d" % index)
        is_faulty = False
        for ing in item["ingredients"]:
            ing["ing_ammount"] = calculate_ammount(ing["ing_ammount"])
            loc_name = check_parity(ing["ing_name"])
            if loc_name is ing["ing_name"]:
                not_found_list.append(ing["ing_name"])
                is_faulty = True
            else:
                ing["ing_name"] = loc_name
        item["faulty"] = is_faulty
    with open("ingredients_clean.txt", "w+") as f:
        f.write(json.dumps({"items": items},  indent=4, sort_keys=True))
    with open("not_found.txt", "w+") as f:
        f.write(json.dumps(not_found_list,  indent=4, sort_keys=True))

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
    ingredients = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "orange juice", "grenadine", "mate")
    for ing in ingredients:
        if ing in ingredient.lower():
            return ing
    return ingredient


if __name__ == "__main__":
    main()