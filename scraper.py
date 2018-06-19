import urllib.error
from urllib.request import urlopen
import json
from bs4 import BeautifulSoup
from parser import parseLinks
from extract import extractInfo

def scrape(baseUrl):

	traverseList = []
	base = baseUrl
	traverseList.insert(0,base)
	limit = 40
	count = 0
	infoList = []

	while(traverseList):

		url = traverseList.pop()
		# print url
		if(not url):
			continue

		try:
			response = urlopen(url)
		except urllib.error.URLError as e:
		 	print(e.reason)
		 	continue

		try:
			webContent = response.read()
		except:
			continue

		soup = BeautifulSoup(webContent,'html.parser')
		aRefs = parseLinks(soup,url,baseUrl)
		info =	extractInfo(url,baseUrl,soup)
		infoList.append(info)

		if(not aRefs):
			continue

		# Add more pages to visit here.
		for tag in aRefs:
			# print tag['href']
			# print '\n'

			try:
				if(baseUrl == 'http://doer.metastudio.org/phet/en/simulations.html'):
					traverseList.append('http://doer.metastudio.org/phet/en/'+tag['href'])
				if(baseUrl == 'http://localhost:8008/learn/khan/'):
					print(aRefs)
			except KeyError:
				print('href tag does not exist')

		print('Checked url ' + url)
		count += 1

	file = open('metadata.json','w')
	json.dump({ 'metadata': infoList },file)
	file.close()
	print('Successfully completed scraping base url' + base + '\n')


def appendProtocol(url):
	if(url[0:4] == 'http' or url[0:5] == 'https'):
		return ''
	else:
		return 'http:'
