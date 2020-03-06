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
		multiplePages = True
		# Start the count at 2 because 1 is the used in default query
		pageNumber = 2

		# Need to loop continuosuly in case there are multiple pages returned
		while multiplePages:
			page = requests.get(self.url, headers=self.headers)
			if page.status_code == 404:
				return self.asosItemDetails

			soup = BeautifulSoup(page.content, 'html.parser')

			# Extract the items
			for line in soup.find_all(class_=self.firstClass):
				for subSearch in line.find_all(class_=self.secondClass):
					link = (subSearch['href'])
					self.asosItemDetails.update({subSearch.text: link.strip()})

			# Check are we on the last page
			amountOfItems = soup.find_all(class_="fWxiz1Y")
			for value in amountOfItems:
				currentItemNumber = int((value.find('progress')['value']))
				totalItemNumber = int((value.find('progress')['max']))

			if currentItemNumber != totalItemNumber:
				self.url = self.url.replace(self.url[len(self.url)-1], str(pageNumber))
				pageNumber += 1
			else:
				multiplePages = False

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