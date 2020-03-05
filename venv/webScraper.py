from getData import getAsosItem
from sendEmail import Email

# Asos Fred Perry Details, items priced between 20 to 50
url = 'https://www.asos.com/search/?currentpricerange=20-340&q=fred%20perry&refine=currentprice:20%3C35'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
firstFredPerryClass = "_3pQmLlY"
secondFredPerryClass = "_3TqU78D"

# Create a Fred Perry Object
fredPerry = getAsosItem(url, headers, firstFredPerryClass, secondFredPerryClass)
# Get the item Details
fredPerryItemDetails = fredPerry.getAsosItemDetails()
# Format the item Detail for email
fredPerryText = fredPerry.formatDetailsForEmail(fredPerryItemDetails)

# Email the details
send = Email(fredPerryText)
send.sendEmail()


