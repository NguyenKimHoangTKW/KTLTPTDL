import requests
from bs4 import BeautifulSoup
import pandas as pd

resp = requests.get("https://4menshop.com/quan-nam.html")
soup = BeautifulSoup(resp.content, "html.parser")
parents = soup.find_all("div", {"class": "product-info"})
data = []
for parent in parents:
    name = parent.find(class_="product-title").get_text(strip=True)
    price = parent.find(class_="product-price").get_text(strip=True)
    formatted_text = f"{name}, {price}"
    data.append([name, price])
    print(formatted_text)

df = pd.DataFrame(data, columns=["Name", "Price"])

df.to_excel("Shop.xlsx",index=False)