import requests
from bs4 import BeautifulSoup
import csv

with open('booktoscrape.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["ID",'Book', 'Price'])
    number = 0
    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, "html.parser")
        parents = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
        for parent in parents:
                number += 1
                element = parent.find("h3")
                result = element.find("a")
                book = result["title"]
                price = parent.find("p", {"class": "price_color"}).get_text()
                format_price = price.replace("£", "$")
                print([number,book, format_price])
                writer.writerow([number,book, format_price])
