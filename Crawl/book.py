import requests
from bs4 import BeautifulSoup
import csv
url = 'https://truyenqqvn.com/truyen-moi-cap-nhat/trang-1.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup)