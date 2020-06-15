from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'

# opening the connection, grabbing the webpage 
uClient = uReq(my_url)

# closing the connection
uClient.close()

# html parser, page_html = uClient.read()
page_soup = soup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll("div", {"class":"item-container"})

# access a specific container (even when theres others behind it (a div thats not the first div in the html))
# container = containers[0]
br_contain = container.findAll("div",{"class":"item-info"})

# get image title
br_contain[0].div.a.img["title"]

for container in containers:
	brand = br_contain[0].div.a.img["title"]
	# this until 22:02 in video: https://www.youtube.com/watch?v=XQgXKtPSzUI&t=1s
	#title container
	title_container = container.findAll("a", {"class": "item-title"})
	product_name = title_container[0].text

	#shipping price
	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	print("brand: "brand)
	print("product name: "product_name)
	print("shipping price": shipping)