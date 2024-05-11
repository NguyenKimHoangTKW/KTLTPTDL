import requests
from bs4 import BeautifulSoup

url = "https://phimmoi.tech/genre/phim-le/page/1"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
phimmoi = soup.find_all("article",{"class": "item movies"})
for movies in phimmoi:
    poster = movies.find("div",{"class": "poster"})
    img = poster.find("img")['src']
    quality = poster.find("div",{"class": "btnRV"}).get_text()
    data = movies.find("div",{"class": "data"})
    link_film = data.find("a")['href']
    name_film = data.find("h3").get_text()
    date = data.find("span").get_text()
    
    url1 = link_film
    thongtinphim = requests.get(url1)
    soup = BeautifulSoup(thongtinphim.content, 'html.parser')
    phimmoi_details = soup.find_all("div",{"class": "sheader"})
    mota_phim = soup.find_all("div",{"class": "sbox"})
    tendienvien = soup.find_all("div",{"class":"sbox fixidtab"})
    for chitietphim in phimmoi_details:
        # Tạo mốt biến là chuỗi để gán dữ liệu
        NameDicr = []
        NamAction = []
        Nam = []
        TheLoai = []
        description = []
        country = chitietphim.find("span",{"class": "country"}).get_text()
        duration = chitietphim.find("span",{"class": "runtime"}).get_text()
        genres = chitietphim.find("div",{"class": "sgeneros"})
        genres = genres.find_all("a")
        # gán genres thành 1 chuỗi
        genres = ', '.join(tag.get_text() for tag in genres)
        # tách chuỗi thành 1 split để dễ dàng lấy chuỗi ra ngoài theo dạng 0,1,2,3,4,...
        genres_list = genres.split(', ')
        # lấy năm bắt đầu từ chuỗi 0
        Nam = genres_list[0]
        TheLoai = genres_list[1::]
        TheLoai = ', '.join(TheLoai)
        for motafilms in mota_phim:
            findmota = motafilms.find("p")
            if findmota:
                description = findmota.get_text()
        # lồng vòng lặp để lấy ra tên Direction từ itemprop director
        for _tendienvien in tendienvien:
            nameDi = _tendienvien.find_all("div", {"itemprop": "director"})
            for _nameDi in nameDi:
                nameDia = _nameDi.find_all("a", {"itemprop": "url"})
                
                for _nameDi in nameDia:
                    NameDicr.append(_nameDi.get_text())
                
        # lồng vòng lặp để lấy ra tên Diễn Viên từ itemprop actor        
            nameAc = _tendienvien.find_all("div", {"itemprop": "actor"})
            for _nameAC in nameAc:
            
                nameAct =_nameAC.find_all("a", {"itemprop": "url"})
                for _nameAc in nameAct:
                    NamAction.append(_nameAc.get_text())
                    

        ActionName = ', '.join(NamAction)
        DirectorName = ', '.join(NameDicr)
    print([name_film, date, quality, country, duration,Nam,TheLoai,DirectorName,ActionName,description])
