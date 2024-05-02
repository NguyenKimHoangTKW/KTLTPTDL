import requests
from bs4 import BeautifulSoup
for page in range(1,2+1):
    url = f"https://truyenqqvn.com/truyen-moi-cap-nhat/trang-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    formattruyen = soup.find_all("ul",{"class","list_grid grid"})
    for items in formattruyen:
        timtruyen = items.find_all("li")
        for parent in timtruyen:
            tentruyen = parent.find("div",{"class","book_info"})
            formattruyen = tentruyen.find("h3")
            tentruyen = formattruyen.get_text()
            linktruyen = formattruyen.find("a")['href']
            tinhtrangtruyen = parent.find_all("p",{"class","info"})
            tinhtrang = tinhtrangtruyen[0].get_text()
            tinhtrang = tinhtrang.replace("Tình trạng: ","")
            luotxem = tinhtrangtruyen[1].get_text()
            luotxem = luotxem.replace("Lượt xem: ","")
            luottheodoi = tinhtrangtruyen[2].get_text()
            luottheodoi = luottheodoi.replace("Lượt theo dõi: ","")
            formattheloai = parent.find("div",{"class","list-tags"})
            theloai = formattheloai.find_all("p")

            theloaitruyen = ', '.join(tag.get_text() for tag in theloai)
            noidungtruyen = parent.find("div",{"class","excerpt"})
            if(noidungtruyen):
                noidung = noidungtruyen.get_text()
            tenkhac = parent.find("div",{"class","title-more-other"})
            if(tenkhac):
                tenkhac1 = tenkhac.get_text()
                print([tentruyen,tenkhac1,linktruyen,tinhtrang,luotxem,luottheodoi,theloaitruyen,noidung])