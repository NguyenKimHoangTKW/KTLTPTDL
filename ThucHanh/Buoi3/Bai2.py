import requests
from bs4 import BeautifulSoup
import csv

with open('info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Tên tác giả', 'Câu nói', 'Ngày sinh', 'Link']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for page in range(1, 2 + 1):
        url = f'https://quotes.toscrape.com/page/{page}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        parent = soup.find_all("div", {"class", "quote"})
        for parents in parent:
            caunoi = parents.find("span", {"class", "text"}).get_text()
            tacgia = parents.find("small", {"class", "author"}).get_text()
            link = parents.find("a")['href']
            link = "https://quotes.toscrape.com/" + link
            urlauthor = link
            response1 = requests.get(urlauthor)
            soup1 = BeautifulSoup(response1.content, 'html.parser')
            author = soup1.find_all("div", {"class", "author-details"})
            for authors in author:
                ngaythangsinh = authors.find("span", {"class", "author-born-date"}).get_text()
                print([tacgia, caunoi, ngaythangsinh, link])
                writer.writerow({'Tên tác giả': tacgia, 'Câu nói': caunoi, 'Ngày sinh': ngaythangsinh, 'Link': link})

