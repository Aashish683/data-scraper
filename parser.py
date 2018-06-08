from extract import extractInfo

def parseLinks(soup,url,baseUrl):
	if(url == baseUrl == 'http://doer.metastudio.org/phet/en/simulations.html'):
		return parseForPhet(soup,baseUrl)
	if(url == baseUrl == 'http://localhost:8008/learn/khan/'):
		return parseForKa(soup,baseUrl)


def parseForPhet(soup,baseUrl):
	tags = soup.find_all('a',class_='simulation-link')
	return tags
def parseForKa(soup,baseUrl):
	print(soup.prettify())
