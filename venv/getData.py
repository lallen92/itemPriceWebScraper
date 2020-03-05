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
		'''
			getAsosItemDetails:		Based off of the chosen brand and price range, return a dictionary containg its information.

			:return: 				A dictionary containing the item details and a link to the item.
		'''
		page = requests.get(self.url, headers=self.headers)
		soup = BeautifulSoup(page.content, 'html.parser')

		for line in soup.find_all(class_=self.firstClass):
			for subSearch in line.find_all(class_=self.secondClass):
				link = (subSearch['href'])
				self.asosItemDetails.update({subSearch.text: link.strip()})

		return self.asosItemDetails

	def formatDetailsForEmail(self, brandItemDetails):
		'''
			getAsosItemDetails:		Extracts the details of each item from the dictionary and adds them to a string to be
									displayed in the email.

			:parameter:				brandItemdDetails - A dictionary of items for the chosen brand
			:return: 				A dictionary containing the item details and a link to the item.
		'''
		brandText = ''
		for key in brandItemDetails:
			brandText += key + ' -> ' + brandItemDetails[key] + " \n"
		return brandText