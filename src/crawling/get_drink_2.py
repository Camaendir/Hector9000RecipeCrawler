from six.moves import urllib
import json
from bs4 import BeautifulSoup
import traceback
import os.path
from src.crawling.get_drinksurls_1 import main as get_drinkurls
# get_drink_2.py
# Using the Urls and Saving all Drink-Data in a txt File
# Ingredients get partially sorted


def main():
    print("Gathering Raw Drink Data")
    if not os.path.isfile("../Savefile/drinkurls.txt"):
        print("Could not find any Drink Urls. Crawling the Internet to get some.")
        get_drinkurls()
    index = 0
    drinklist = []
    drinkurls = []
    with open("../Savefiles/drinkurls.txt", "r") as file:
        for line in file.readlines():
            drinkurls.append(line.rstrip('\n'))
    try:
        for url in drinkurls:
            index = index + 1
            print("Loading Drink Nr. %d" % index)
            loaddrink(url, drinklist)
        print("Loaded and Saved %d Drinks" % index)
    except Exception:
        print("Error in Loading. Saving Index")
        traceback.print_exc()
        savejson(drinklist, index)
        return None
    savejson(drinklist)
    print("Gathering Raw Drink Data Complete")
    return generatejson(drinklist)


def generatejson(drinklist):
    return json.dumps({"items": drinklist}, indent=4, sort_keys=True)


def savejson(drinklist, index=None):
    if index is None:
        Saveindex = False
    else:
        Saveindex = True
    with open("../Savefiles/drinks_raw_full.txt", "w+") as f:
        f.write(generatejson(drinklist))
    if Saveindex:
        f.write("\n")
        f.write(str(index))


def loaddrink(url, drinklist):
    raw_ingredients = ("gin", "rum", "vodka", "tequila", "tonic", "coke", "orange juice", "grenadine", "mate", "cola")
    ingredients = []
    try:
        name = url.replace("https://www.socialandcocktail.co.uk/cocktails/", "").replace("/", "")
        page = urllib.request.urlopen(url)
        html = BeautifulSoup(page, "html.parser")
        itemlist = html.find(id="content-to-load").p
        full_body = itemlist
        for ingredient in itemlist.string.split(","):
            if "ml" not in ingredient:
                for ing in raw_ingredients:
                    if ing in ingredient.lower():
                        ingredients.append({"ing_ammount": "TBD", "ing_name": ing, "Purity": 2, "body": ingredient})
                        continue
                ingredient.append({"body": ingredient, "Purity": 3})
                continue
            split = ingredient.split("ml ")
            ingredients.append({"ing_ammount": split[0] + "ml", "ing_name": split[1], "Purity": 1})
        drinklist.append({"drink_name": name, "ingredients": ingredients, "full_body": full_body})
    except:
        print("Error in loaddrink; URL: %s" % url)


if __name__ == "__main__":
    main()
