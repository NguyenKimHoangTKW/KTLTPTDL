import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hoang",
)
cursor = db.cursor()
def create_or_connect_database():
    try:
        cursor.execute("USE dbthptqg2023")
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            cursor.execute("CREATE DATABASE dbthptqg2023")
            db.commit()
            print("Database đã được tạo thành công")
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
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS `dblthongtinthisinh` (
                `sbd` varchar(20) NOT NULL,
                `macumthi` varchar(20) DEFAULT NULL,
                `toan` float DEFAULT NULL,
                `nguvan` float DEFAULT NULL,
                `ngoaingu` float DEFAULT NULL,
                `vatly` float DEFAULT NULL,
                `hoahoc` float DEFAULT NULL,
                `sinhhoc` float DEFAULT NULL,
                `lichsu` float DEFAULT NULL,
                `dialy` float DEFAULT NULL,
                `gdcd` float DEFAULT NULL,
                `diemtb` float DEFAULT NULL,
                `urlweb` varchar(2000) DEFAULT NULL,
                PRIMARY KEY (`sbd`),
                KEY `fk_macumthi_idx` (`macumthi`),
                CONSTRAINT `fk_macumthi` FOREIGN KEY (`macumthi`) REFERENCES `cumthi` (`Macumthi`) ON DELETE CASCADE ON UPDATE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
        """)
        db.commit()
    except mysql.connector.Error as err:
        print(err.msg)

create_table()

start = 2040868
end = 2040870
added_cumthi = set()

async def fetch_data(session, sobaodanh):
    sobaodanh = str(sobaodanh).zfill(8)
    url = f"https://diemthi.vnexpress.net/index/detail/sbd/{sobaodanh}/year/2023"
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        parent = soup.find_all("div", {"class": "o-detail-thisinh"})
        for parents in parent:
            try:
                sobaodanh = parents.find("h2", {"class": "o-detail-thisinh__sbd"}).get_text()
                sobaodanh = re.search(r'\b\d+\b', sobaodanh).group()
                subject_cumthi = parents.find("p", {"class": "o-detail-thisinh__cumthi"}).get_text()
                score_cumthi = re.search(r'\b\d+\b', subject_cumthi).group()
                cumthi_name = subject_cumthi.split(" - ")[1] 
                data = [sobaodanh, score_cumthi, cumthi_name]
                findmonhoc = parents.find("div", {"class": "o-detail-thisinh__diemthi"})
                monhoc = findmonhoc.find_all("tr")
                subjects = ["Toán", "Ngữ văn", "Ngoại ngữ", "Vật lý", "Hóa học", "Sinh học", "Lịch sử", "Địa lý", "Giáo dục công dân"]
                subject_scores = {subject: "NULL" for subject in subjects}
                tong_score = 0
                dem_score = 0
                for row in monhoc:
                    cells = row.find_all("td")
                    if len(cells) == 2:
                        subject_name = cells[0].get_text().strip()
                        subject_score = cells[1].get_text().strip()
                        if subject_name in subjects:
                            subject_scores[subject_name] = subject_score
                            if subject_score != "NULL":
                                tong_score += float(subject_score)
                                dem_score += 1
                data.extend(subject_scores.values())
                if tong_score > 0:
                    DiemTB = round(tong_score / dem_score, 2)
                else:
                    DiemTB = None
                data.append(DiemTB)
                data.append(url)
                print(data)           
                if score_cumthi not in added_cumthi:
                    cursor.execute("INSERT INTO cumthi (Macumthi, tencumthi) VALUES (%s, %s) ON DUPLICATE KEY UPDATE tencumthi = VALUES(tencumthi)", (score_cumthi, cumthi_name))
                    added_cumthi.add(score_cumthi)
                cursor.execute("REPLACE INTO dblthongtinthisinh (sbd, macumthi, toan, nguvan, ngoaingu, vatly, hoahoc, sinhhoc, lichsu, dialy, gdcd, diemtb, urlweb) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                                (sobaodanh, score_cumthi, 
                                    data[3] if data[3] != "NULL" else None, 
                                    data[4] if data[4] != "NULL" else None, 
                                    data[5] if data[5] != "NULL" else None, 
                                    data[6] if data[6] != "NULL" else None, 
                                    data[7] if data[7] != "NULL" else None, 
                                    data[8] if data[8] != "NULL" else None, 
                                    data[9] if data[9] != "NULL" else None, 
                                    data[10] if data[10] != "NULL" else None, 
                                    data[11] if data[11] != "NULL" else None, 
                                    DiemTB if DiemTB != "NULL" else None, 
                                    url))
            except AttributeError:
                pass
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, sobaodanh) for sobaodanh in range(start, end + 1)]
        await asyncio.gather(*tasks)


asyncio.run(main())
db.commit()
cursor.close()
db.close()