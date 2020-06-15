# it grab the html content
from urllib.request import urlopen as uReq

# It parse the html text
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic%20cards'

# Opening the connection and grabbing the page
uClient = uReq(my_url)

# store as read, because it will dump them after read
page_html = uClient.read()

# close connection
uClient.close()

# html parser
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"

f = open(filename, "w")

headers = "product_brand, product_name, product_shipping\n"

f.write(headers)

for container in containers:
    try:
        brand = container.find("div", "item-info").div.a.img["title"]
    except Exception as e:
        brand = "NA"
    else:
        pass
    finally:
        pass

    title_container = container.findAll("a", {"class": "item-title"})

    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})

    shipping = shipping_container[0].text.strip()

    # print("product_brand: " + product_brand)
    # print("product_name: " + product_name)
    # print("product_shipping: " + product_shipping)

    # replace "," in product name with "|"
    f.write(product_name.replace(",", "|") + "," + brand + "," + shipping + "\n")

f.close()
