from six.moves import urllib
from bs4 import BeautifulSoup
from pathlib import Path
# get_drinksurls_1.py
# Saving all Drink URL's in a txt file

baseurl = "https://www.socialandcocktail.co.uk/cocktail-recipes/page/%PAGE%/?sort_by=title&sort_name=Name&custom_sort=0&sort=ASC"
pagetext = "%PAGE%"
drinks = []
drinkurls = []
exceptions = ("https://www.socialandcocktail.co.uk/cocktails/tommys-margarita/")


def load_page(page):
	page = urllib.request.urlopen(baseurl.replace("%PAGE%", str(page)))
	html = BeautifulSoup(page, "html.parser")
	localdrinks = html.find_all("div", "recipe_summary pjax")
	if len(localdrinks) is 0:
		return True
	for dr in localdrinks:
		href = dr.findAll("a")[0]["href"];
		if href in exceptions:
			continue
		drinkurls.append(href)
	return False


def main():
	print("Gathering Drink Urls")
	index = 0
	while True:
		index = index + 1
		print("Load page Nr. %d" % index)
		if load_page(index):
			break
	print("Loaded %d Pages" % index)
	print("Saving %d Urls to file" % len(drinkurls))
	file = open(Path("../Savefiles/drinkurls.txt"), "w+")
	for i in drinkurls:
		file.write(i)
		file.write("\n")
	file.close()
	print("Drink-Url-Gathering complete")
	return drinkurls


if __name__ == "__main__":
	main()