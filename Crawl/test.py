import requests
from bs4 import BeautifulSoup

url = "https://truyenqqvn.com/truyen-tranh/gia-toc-diep-vien-yozakura-8043"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
titletruyen = soup.find("div",{"class","story-detail-info detail-content"})
tieudetruyen= titletruyen.find("p").get_text()
print(tieudetruyen)   
