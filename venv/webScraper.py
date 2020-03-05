import requests
from bs4 import BeautifulSoup

class getAsosItem:
	def __init__(self, url, headers, firstClass, secondClass):
		self.url = url
		self.headers = headers
		self.firstClass = firstClass
		self.secondClass = secondClass
		self.asosItemDetails = {}

	def getAsosItemDetails(self):
		page = requests.get(self.url, headers=self.headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		for line in soup.find_all(class_=self.firstClass):
			for subSearch in line.find_all(class_=self.secondClass):
				link = (subSearch['href'])
				self.asosItemDetails.update({subSearch.text: link.strip()})

			return self.asosItemDetails

# Asos Fred Perry Details, items priced between 20 to 50
url = 'https://www.asos.com/search/?currentpricerange=20-340&q=fred%20perry&refine=currentprice:20%3C35'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
firstFredPerryClass = "_3pQmLlY"
secondFredPerryClass = "_3TqU78D"

fredPerry = getAsosItem(url, headers, firstFredPerryClass, secondFredPerryClass)

for key in fredPerry.getAsosItemDetails():
	print(key, '->', fredPerry.getAsosItemDetails()[key])

