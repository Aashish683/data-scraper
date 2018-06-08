from scraper import scrap

# ''http://doer.metastudio.org/phet/en/simulations.html''
BASE_URL_List = ['http://localhost:8008/learn/khan/']

for base in BASE_URL_List:
	scrap(base)
