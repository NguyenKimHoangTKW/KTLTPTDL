import requests
from bs4 import BeautifulSoup

url1 = "https://phimmoi.tech/movies/nhat-my-tro-ve/"
thongtinphim = requests.get(url1)
soup = BeautifulSoup(thongtinphim.content, 'html.parser')
phimmoi_details = soup.find_all("div",{"class": "sheader"})
mota_phim = soup.find_all("div",{"class": "sbox"})
tendienvien = soup.find_all("div",{"class":"sbox fixidtab"})
for chitietphim in phimmoi_details:
    country = chitietphim.find("span",{"class": "country"}).get_text()
    duration = chitietphim.find("span",{"class": "runtime"}).get_text()
    genres = chitietphim.find("div",{"class": "sgeneros"})
    genres = genres.find_all("a")
    genres = ', '.join(tag.get_text() for tag in genres)
    genres_list = genres.split(', ')
    genres_year = genres_list[0]
    for motafilms in mota_phim:
        findmota = motafilms.find("p")
        if findmota:
            description = findmota.get_text()
    NameDicr = []
    NamAction = []
    for _tendienvien in tendienvien:
        
        nameDi = _tendienvien.find_all("div", {"itemprop": "director"})
        for _nameDi in nameDi:
            nameDia = _nameDi.find_all("a", {"itemprop": "url"})
            
            for _nameDi in nameDia:
                NameDicr.append(_nameDi.get_text())
            
            
        nameAc = _tendienvien.find_all("div", {"itemprop": "actor"})
        for _nameAC in nameAc:
        
            nameAct =_nameAC.find_all("a", {"itemprop": "url"})
            for _nameAc in nameAct:
                NamAction.append(_nameAc.get_text())
                

    ActionName = ', '.join(NamAction)
    DirectorName = ', '.join(NameDicr)
    print([DirectorName,ActionName])
    
    
            

                
       
   
          

