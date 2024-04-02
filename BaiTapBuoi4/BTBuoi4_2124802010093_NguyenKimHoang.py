import mysql.connector
bai1=""
bai2=""
bai3=""
bai4=""
bai5=""
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="dbquanlydean")
cursor = db.cursor()
#1
cursor.execute(
    "SELECT nv.tennv FROM thamgia tg, nhanvien nv where nv.manv = tg.manv and tg.mada = 1"
    )
thamgia = cursor.fetchall()

for thamgias in thamgia:
    bai1 += f" {thamgias}"  
print("1. Danh sách nhân viên tham gia dự án Phần mềm quản lý trường học là :",bai1)

#2
cursor.execute(
    "SELECT nv.tennv, nv.tuoi from nhanvien nv where nv.gioitinh = 1"
    )
nhanviennu = cursor.fetchall()

for nhanviennus in nhanviennu:
    bai2 += f" {nhanviennus}"  
print("2. Danh sách biết thông tin nhân viên Nữ :",bai2)
#3
cursor.execute(
    "SELECT nv.tennv from thamgia tg, nhanvien nv, duan da where nv.manv = tg.manv and da.mada = tg.mada and da.tenda = 'Hệ thống dự báo thời tiết' and nv.gioitinh = 1"
    )
nhanvien = cursor.fetchall()

for nhanviens in nhanvien:
    bai3 += f" {nhanviens}"  
print("3. Danh sách nhân viên Nam tham gia dự án Hệ thống dự báo thời tiết:",bai3)

#4
cursor.execute(
    "SELECT DISTINCT da.tenda, da.ngaybd, da.ngaykt from duan da, thamgia tg where da.mada = tg.mada and tg.ngayradu IS NULL"
    )
duan = cursor.fetchall()

for duans in duan:
    tenda = duans[0]
    ngaybd = duans[1].strftime("%d-%m-%Y") if duans[1] else "N/A"
    bai4 += f" ({tenda}, {ngaybd})"
print("4. Danh sách thông tin dự án chưa có kết thúc:",bai4)
#5
cursor.execute(
    "SELECT DISTINCT nv.tennv , nv.tuoi, CASE WHEN nv.gioitinh = '0' THEN 'Nam' ELSE 'Nữ' END from thamgia tg, nhanvien nv where nv.manv = tg.manv"
    )
nhanvienthamgia = cursor.fetchall()

for nhanvienthamgias in nhanvienthamgia:
     bai5 += f" {nhanvienthamgias}"  
print("5. Danh sách thông tin nhân viên còn đang tham gia dự án:",bai5)
cursor.close()
db.close()