from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen("http://www.pythonscraping.com/pages/page3.html")


soup = BS(html, 'html.parser')
print(soup)
for sibling in soup.find("table",{"id" : "giftList"}).tr.next_siblings:
    print(sibling)


# soup.find_all("p")