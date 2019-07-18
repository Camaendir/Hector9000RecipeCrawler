import os.path
import get_drinks
from six.moves import urllib
import json
from bs4 import BeautifulSoup
import traceback

# get_ingredients.py

def main(usetxt, savefile=None):
    index = 1
    drinklist = []
    shortdrinklist = []
    if savefile is None:
        savefile = False
    if usetxt:
        if not os.path.exists("drinkurls.txt"):
            usetxt = False
            print("File doesnt exist")
    drinkurls = []
    if usetxt:
        with open("drinkurls.txt", "r") as file:
            for line in file.readlines():
                drinkurls.append(line.rstrip('\n'))
    else:
        drinkurls = get_drinks.main(False)
    print("Get Drink Urls")
    try:
        for url in drinkurls:
            print("Loading Drink Nr. %d" % index)
            loaddrink(url, drinklist, shortdrinklist)
            index = index + 1
            if index % 100 is 0:
                save100(shortdrinklist, index / 100)
                shortdrinklist = []
    except Exception:
        print("Error in Loading. Saving Index")
        traceback.print_exc()
        savejson(True)
    if savefile:
        savejson(drinklist)
    else:
        return generatejson(drinklist)


def save100(shortdrinklist, index):
    with open(("ingredients_raw_%d00.txt" % index), "w+") as f:
        f.write(generatejson(shortdrinklist))
        print("saved 100 drinks")


def generatejson(drinklist):
    return json.dumps({"items": drinklist}, indent=4, sort_keys=True)


def savejson(drinklist, Saveindex=None):
    if Saveindex is None:
        Saveindex = False
        with open("ingredients_raw.txt", "w+") as f:
            f.write(generatejson(drinklist))
        if Saveindex:
            f.write("\n")
            f.write(str(index))
        print("Saved Json to File")


def loaddrink(url, drinklist, shortdrinklist):
    json = ""
    ingredients = []
    try:
        name = url.replace("https://www.socialandcocktail.co.uk/cocktails/", "").replace("/", "")
        page = urllib.request.urlopen(url)
        html = BeautifulSoup(page, "html.parser")
        itemlist = html.find(id="content-to-load").p
        for ingredient in itemlist.string.split(","):
            if "ml" not in ingredient:
                continue
            split = ingredient.split("ml ")
            ingredients.append({"ing_ammount": split[0] + "ml", "ing_name": split[1]})
        drinklist.append({"drink_name": name, "ingredients": ingredients})
        shortdrinklist.append({"drink_name": name, "ingredients": ingredients})
    except:
        print("Error in loaddrink; URL: %s" % url)


if __name__ == "__main__":
    index = 1
    main(True, True)