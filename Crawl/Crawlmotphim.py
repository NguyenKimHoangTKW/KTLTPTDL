import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd 
data = []

with open('MotPhim.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Tên tiếng việt', 'Tên tiếng anh', 'Image', 'Trạng thái', 'Ngày phát hành', 'Thời lượng phim', 'Quốc gia', 'Thể loại phim', 'Mô tả phim', 'URL phim'])
    for page in range(1, 2+1):  # Sửa số trang tùy theo yêu cầu
        url = f"https://motphimww.com/phim-le/page/{page}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        movies = soup.find_all("article", {"class", "item movies"})
        for movie in movies:
            findposter = movie.find("div", {"class", "poster"})
            img = findposter.find("img")['src']
            trangthaifilm = movie.find("div", {"class", "trangthai"}).get_text()
            linkfilm = findposter.find("a")['href']
            finddatafilm = movie.find("div", {"class", "data"})
            tentiengviet = finddatafilm.find("h3").get_text()
            tentienganh = finddatafilm.find("span").get_text()
            url1 = linkfilm
            getthongtinphim = requests.get(url1)
            soup1 = BeautifulSoup(getthongtinphim.content, 'html.parser')
            movie = soup1.find_all("div", {"class", "sheader"})
            motafilm = soup1.find_all("div", {"class", "sbox"})
            for movies in movie:
                ngayphathanh = movies.find("span", {"class", "date"}).get_text()
                thoiluongfilm = movies.find("span", {"class", "runtime"})
                if thoiluongfilm:
                    thoiluongfilm = thoiluongfilm.get_text()
                else:
                    pass
                quocgia = movies.find("span", {"class", "country"}).get_text()
                theloaifilm = movies.find("div", {"class", "sgeneros"})
                theloaifilm = theloaifilm.find_all("a")
                theloaifilm = ', '.join(tag.get_text() for tag in theloaifilm)
            for motafilms in motafilm:
                findmota = motafilms.find("p")
                if findmota:
                    mota1 = findmota.get_text()
                    print([tentiengviet, tentienganh, img, trangthaifilm, ngayphathanh, thoiluongfilm, quocgia, theloaifilm, mota1, url1])
                    csv_writer.writerow([tentiengviet, tentienganh, img, trangthaifilm, ngayphathanh, thoiluongfilm, quocgia, theloaifilm, mota1, url1])
                    data.append([tentiengviet, tentienganh, img, trangthaifilm, ngayphathanh, thoiluongfilm, quocgia, theloaifilm, mota1, url1])


df = pd.DataFrame(data, columns=['Tên tiếng việt', 'Tên tiếng anh', 'Image', 'Trạng thái', 'Ngày phát hành', 'Thời lượng phim', 'Quốc gia', 'Thể loại phim', 'Mô tả phim', 'URL phim'])

df.to_excel('MotPhim.xlsx', index=False)