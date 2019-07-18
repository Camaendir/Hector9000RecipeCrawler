from six.moves import urllib
from bs4 import BeautifulSoup

# get_drinks.py

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


def main(safefile=None):
	if safefile is None:
		safefile = False
	index = 1
	while True:
		print("Load page Nr. %d" % index)
		if load_page(index):
			break
		index = index + 1
	if safefile:
		print("Saving %d urls to file" % len(drinkurls))
		file = open("drinkurls.txt", "w+")
		for i in drinkurls:
			file.write(i)
			file.write("\n")
		file.close()
	else:
		print("returning %d urls" % len(drinkurls))
		return drinkurls


if __name__ == "__main__":
	main(True)