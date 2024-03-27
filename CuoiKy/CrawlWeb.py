import requests
from bs4 import BeautifulSoup
import pandas as pd

resp = requests.get("https://vnexpress.net/kinh-doanh/doanh-nghiep")
soup = BeautifulSoup(resp.content, "html.parser")
parents = soup.find_all("div", {"class": "width_common list-news-subfolder has-border-right"})
result = parents[0].find_all("a")
for i in result:
    elements = i.get_text(strip=True)
    print(elements)