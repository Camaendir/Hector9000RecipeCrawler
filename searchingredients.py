from six.moves import urllib
from bs4 import BeautifulSoup

#searchingredients.py
baseurl = "https://www.socialandcocktail.co.uk/cocktail-recipes/page/%PAGE%/?sort_by=title&sort_name=Name&custom_sort=0&sort=ASC"
pagetext = "%PAGE%"
drinks = []
drinkurls = []

def loadpage(page):
	page = urllib.request.urlopen(baseurl.replace("%PAGE%", str(page)))
	html = BeautifulSoup(page)
	localdrinks = html.find_all("div", "recipe_summary pjax")
	if len(localdrinks) == 0:
		return True
	for dr in localdrinks:
		drinkurls.append(dr.findAll("a")[0]["href"])
	return False

def main():
	index = 1
	while True:
		if loadpage(index):
			break
		if index == 2:
			break
		index = index + 1
	for i in drinkurls:
		print(i)

if __name__ == "__main__":
	main()
