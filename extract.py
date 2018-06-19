

class References:
	def __init__(self):
		# 0-> Elementary, 1 -> Middle 2-> High 3 -> University
		self.gradeLevel = []
		self.name = ''
		self.keywords = []
		self.description = ''
		self.relatedSimulations = []
		self.credits = {
			'designTeam': [],
			'thirdPartyLibs': [],
			'thanksTo': []
		}

def extractInfo(url,baseUrl,soup):
	# Assuming there will be no info in the baseUrl
	if(url == baseUrl):
		return None
	if(baseUrl == 'http://doer.metastudio.org/phet/en/simulations.html'):
		return extractForPhet(soup)


def extractForPhet(soup):
	ref = References()

	ref.name = soup.find('title').string

	elem = soup.find('a',{'id': 'nav-location-nav-elementary-school'})
	if(elem and elem.span['class'] == [u'nml-link-label', u'selected']):
		ref.gradeLevel.append('Elemenentary')

	middle = soup.find('a',{'id': 'nav-location-nav-middle-school'})
	if(middle and middle.span['class'] == [u'nml-link-label', u'selected'] ):
		ref.gradeLevel.append('Middle')

	high = soup.find('a',{'id': 'nav-location-nav-high-school'})
	if(high and high.span['class'] == [u'nml-link-label', u'selected']):
		ref.gradeLevel.append('High')

	university = soup.find('a',{'id': 'nav-location-nav-university'})
	if(university and university.span['class'] == [u'nml-link-label', u'selected']):
		ref.gradeLevel.append('University')

	keywords = soup.select('.simulation-main-description span[itemprop="keywords"]')
	for keyword in keywords:
		ref.keywords.append(keyword.string)

	description = soup.select('#about p')
	if(description):
		ref.description = description[0].string

	relatedSimulations = soup.select('#related-sims span.simulation-list-title')
	for relatedSimulation in relatedSimulations:
		ref.relatedSimulations.append(relatedSimulation.string)

	creditCategories = soup.select('#credits td ul')
	print(ref.name + '\n')
	print(ref.gradeLevel)
	print(ref.keywords)
	print(ref.description)
	print(ref.relatedSimulations)
	print('\n')
	return ref
