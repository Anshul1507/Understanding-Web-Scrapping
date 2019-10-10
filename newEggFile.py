from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#opening up connection, grabbing the page
uClient = uReq(my_url)
#loads the html data in the variables
page_html = uClient.read()
uClient.close()

#HTML parsing
page_soup = soup(page_html,"html.parser")

#returns heading 
page_soup.h1

page_soup.p

page_soup.body.span

#returns all item-container
containers = page_soup.findAll("div",{"class":"item-container"})

#count the items in container
# len(containers)

# #store the whole data of first container to contain variable
# contain = containers[0]
# container = containers[0]

# #shows the data inside a/div tag
# container.a
# container.div

for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a",{"class":"item-title"})
	product_name = title_container[0].text

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping_name = shipping_container[0].text.strip()

	print("brand: " + brand)
	print("product_name: " + product_name)
	print("shipping_name: " + shipping_name)

    

