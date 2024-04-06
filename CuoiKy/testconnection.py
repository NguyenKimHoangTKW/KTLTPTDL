import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="dbthptqg2023"
    )
    
    if db.is_connected():
        print("Kết nối đến cơ sở dữ liệu thành công!")
    
    db.close()
    print("Đã đóng kết nối đến cơ sở dữ liệu.")
    
except mysql.connector.Error as err:
    print(f"Lỗi khi kết nối đến cơ sở dữ liệu: {err}")
