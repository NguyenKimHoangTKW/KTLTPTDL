import requests
from bs4 import BeautifulSoup
import csv
number = 0
url = f"https://books.toscrape.com/catalogue/page-1.html"
resp = requests.get(url)
soup = BeautifulSoup(resp.content, "html.parser")
parents = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
for parent in parents:
    element = parent.find("h3")
    result = element.find("a")
    book = result["title"]
    price = parent.find("p", {"class": "price_color"}).get_text()
    format_price = price.replace("£", "$")
        #print(book)
    number += 1
    print([number,book, format_price])
        #writer.writerow([number,book, format_price])
