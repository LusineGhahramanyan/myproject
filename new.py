
# request for HTML document of given url
r = requests.get(URL, headers=headers)

# make a soup object by using beautiful
# soup and set the markup as html parser
soup = BeautifulSoup(r.content, 'html.parser')

#create a list of matching elements, in this case all items
orders = soup.findAll(class_="g-item-details")

#used for loop to get last 5 items,  prices and ratings of last 5 items
total = 0
cnt = 0
rating_list = []
