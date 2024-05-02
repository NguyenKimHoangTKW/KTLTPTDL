import requests
from bs4 import BeautifulSoup
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = db.cursor()

def create_or_connect_database():
    try:
        cursor.execute("USE dbthptqg2023")
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            cursor.execute("CREATE DATABASE dbthptqg2023")
            db.commit()
            cursor.execute("USE dbthptqg2023")
        else:
            print(err.msg)
            exit(1)

create_or_connect_database()
def create_table():
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `cumthi` (
                `Macumthi`varchar(20) NOT NULL,
                `tencumthi` varchar(200) DEFAULT NULL,
                PRIMARY KEY (`Macumthi`)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        db.commit()
    except mysql.connector.Error as err:
        print(err.msg)
create_table()
url = "https://motphimww.com/phim-le/phim-john-wick-phan-4-15472"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
movie = soup.find_all("div",{"class","sheader"})
motafilm = soup.find_all("div",{"class","sbox"})
for movies in movie:
    ngayphathanh = movies.find("span",{"class","date"}).get_text()
    thoiluongfilm = movies.find("span",{"class","runtime"}).get_text()
    quocgia = movies.find("span",{"class","country"}).get_text()
    theloaifilm = movies.find("div",{"class","sgeneros"})
    formattheloaifilm = theloaifilm.find_all("a")
    theloaifilm = ', '.join(tag.get_text() for tag in formattheloaifilm)
    for motafilms in motafilm:
        findmota = motafilms.find("p")
        if findmota:
            mota1 = findmota.get_text()
            print([mota1,ngayphathanh])
            