import json

# clean_and_sort.py


def main():
    text = open("ingredients_raw.txt", "r").read()
    items = json.loads(text).items
    index = 0
    for item in items:
        for ing in item["ingredients"]:
            ing["ing_ammount"] = calculate_ammount(ing["ing_ammount"])
            loc_name =   #weitermachen

def calculate_ammount(ammout_str):
    ammout_str = ammout_str.replace("ml", "")
    ammout_str = ammout_str.replace(" ", "")
    pos = ammout_str.find('/')
    if pos is not -1:
        teiler = ammout_str[pos + 1]
        ammout_str = ammout_str.replace("1/" + teiler, "")
        return str(float(ammout_str) + (float(1) / teiler))
    return ammout_str


def check_parity(ingredient):
    ingredients = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "orange juice", "grenadine", "mate")
    for ing in ingredients:
        if ing in ingredient.lower():
            return ing
    return ingredient


if __name__ == "__main__":
    main()