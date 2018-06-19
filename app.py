from scraper import scrape

BASE_URL_List = ['http://doer.metastudio.org/phet/en/simulations.html']

for base in BASE_URL_List:
	scrape(base)
