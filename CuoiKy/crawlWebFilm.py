import requests
from bs4 import BeautifulSoup
import pandas as pd
data = []
for page in range(1, 5):
    url = f"https://phimmoichillp.net/list/phim-le/page-{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movies = soup.find_all('li', class_='item small')
    for movie in movies:
        name_film = movie.find("h3").get_text()
        title_film = movie.find("span", {"class": "label"}).get_text()
        image_film = movie.find("img")["src"]
        link_film = movie.find("a")["href"]
        get_title_link_film = requests.get(link_film)
        soup1 = BeautifulSoup(get_title_link_film.content, 'html.parser')
        link_film = soup1.find("link", {"rel": "canonical"})['href']  
        metadata = soup1.find("ul", {"class": "entry-meta block-film"})
        metadata_items = metadata.find_all("li")
        nam = ''
        theloai = ''
        thoiluong = ''
        dienvien = ''
        for row in metadata_items:
            label = row.find("label")
            if label.get_text() == "Năm Phát Hành: ":
                nam = row.find('a').get_text()
            if label.get_text() == "Thể loại: ":
                formattheloai = row.find_all('a')
                theloai = ', '.join(tag.get_text() for tag in formattheloai)
            if label.get_text() == "Thời lượng: ":
                thoiluong = row.get_text().replace("Thời lượng: ", "")
            if label.get_text() == "Diễn viên: ":
                formatdienvien = row.find_all('a')
                dienvien = ', '.join(tag.get_text() for tag in formatdienvien)
        
        print([name_film, nam, theloai, title_film, thoiluong, dienvien, link_film, image_film])
        data.append([name_film, nam, theloai, title_film, thoiluong, dienvien, link_film, image_film])
df = pd.DataFrame(data, columns=['Name', 'Year', 'Genre', 'Title', 'Duration', 'Actors', 'Link', 'Image'])
df.to_csv('movies_data.csv', index=False, encoding='utf-8-sig')

