import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="hoang",
)

cursor = conn.cursor()
create_database_query = "CREATE DATABASE IF NOT EXISTS quanlynhaphang"
cursor.execute(create_database_query)
use_database_query = "USE quanlynhaphang"
cursor.execute(use_database_query)

# Tạo bảng LoaiHang
create_table_query = """
    CREATE TABLE IF NOT EXISTS LoaiHang (
        MaLoaiHang INT PRIMARY KEY,
        TenLoaiHang NVARCHAR(60) NOT NULL,
        MoTa NVARCHAR(100)
    )
"""
cursor.execute(create_table_query)

# Thêm dữ liệu vào bảng LoaiHang
insert_data_query = """
    INSERT INTO LoaiHang (MaLoaiHang, TenLoaiHang) VALUES 
    (1, 'Tivi'),
    (2, 'Máy lạnh'),
    (3, 'Tủ lạnh'),
    (4, 'Bút đỏ'),
    (5, 'Cục tẩy'),
    (6, 'Bút Xóa'),
    (7, 'Tivi')
"""
cursor.execute(insert_data_query)

# Tạo bảng NhaCungCap
create_table_query = """
    CREATE TABLE IF NOT EXISTS NhaCungCap (
        MaNhaCungCap INT PRIMARY KEY,
        TenNhaCungCap NVARCHAR(30) NOT NULL,
        TenNguoiLienLac NVARCHAR(50) NOT NULL,
        DiaChi NVARCHAR(200) NOT NULL
    )
"""
cursor.execute(create_table_query)

# Thêm dữ liệu vào bảng NhaCungCap
insert_data_query = """
    INSERT INTO NhaCungCap (MaNhaCungCap, TenNhaCungCap, TenNguoiLienLac, DiaChi) VALUES 
    (1, 'Thanh Long', 'Nguyễn Kim Hoàng', 'Trung Quốc'),
    (2, 'Bạch Hổ', 'Nguyễn Thành Long', 'Trung Quốc'),
    (3, 'Chu Tước', 'Đào Thị Huỳnh Trang', 'Trung Quốc'),
    (4, 'Huyền Vũ', 'Nguyễn Huỳnh Linh Đan', 'Việt Nam'),
    (5, 'Dragon Ball', 'Đào Duy Tân', 'Nhật Bản'),
    (6, 'Thiên Long', 'Huỳnh Thị Đào', 'Lộc Ninh'),
    (7, 'Thiên Long Nhân', 'Đào Duy Thanh', 'Lộc Ninh')
"""
cursor.execute(insert_data_query)

# Tạo bảng HangHoa
create_table_query = """
    CREATE TABLE IF NOT EXISTS HangHoa (
        MaHangHoa NVARCHAR(5) PRIMARY KEY,
        TenHangHoa NVARCHAR(60) NOT NULL,
        MaNhaCungCap INT NOT NULL,
        MaLoaiHang INT NOT NULL,
        DonViTinh NVARCHAR(20) NOT NULL,
        DonGia DECIMAL(18, 2) NOT NULL,
        SoLuongTon INT NOT NULL,
        SoLuongDatHang INT NOT NULL,
        FOREIGN KEY(MaNhaCungCap) REFERENCES NhaCungCap(MaNhaCungCap),
        FOREIGN KEY(MaLoaiHang) REFERENCES LoaiHang(MaLoaiHang)
    )
"""
cursor.execute(create_table_query)

# Thêm dữ liệu vào bảng HangHoa
insert_data_query = """
    INSERT INTO HangHoa (MaHangHoa, TenHangHoa, MaNhaCungCap, MaLoaiHang, DonViTinh, DonGia, SoLuongTon, SoLuongDatHang) VALUES 
    ('HH1', 'Tivi Màu', 1, 1, 'Chiếc', 5.00, 50, 20),
    ('HH2', 'Máy lạnh Toshiba', 2, 2, 'Chiếc', 5.00, 30, 10),
    ('HH3', 'Tủ lạnh đẹp', 3, 3, 'Chiếc', 1000000.00, 40, 15),
    ('HH4', 'Bút đỏ hàng Limited', 5, 4, 'Cây', 20.00, 60, 25),
    ('HH5', 'Tẩy hàng Limited', 2, 5, 'Cục', 18.00, 35, 12),
    ('HH6', 'Bút xóa hàng Limited', 7, 6, 'Cây', 22.00, 45, 18),
    ('HH7', 'Tivi 42inch', 1, 7, 'Chiếc', 13000000.00, 55, 22)
"""
cursor.execute(insert_data_query)

# Tạo bảng PhieuNhap
create_table_query = """
    CREATE TABLE IF NOT EXISTS PhieuNhap (
        MaPhieuNhap INT PRIMARY KEY,
        NgayNhap DATETIME NOT NULL,
        MaNhaCungCap INT NOT NULL,
        ThanhTien DECIMAL(18, 2) NOT NULL,
        FOREIGN KEY(MaNhaCungCap) REFERENCES NhaCungCap(MaNhaCungCap)
    )
"""
cursor.execute(create_table_query)

# Thêm dữ liệu vào bảng PhieuNhap
insert_data_query = """
    INSERT INTO PhieuNhap (MaPhieuNhap, NgayNhap, MaNhaCungCap, ThanhTien) VALUES 
    (1, '2023-04-10', 1, 2000.00),
    (2, '2023-04-11', 2, 2500.00),
    (3, '2023-04-12', 3, 3000.00),
    (4, '2023-04-07', 1, 2100.00),
    (5, '2023-04-08', 2, 2700.00),
    (6, '2024-04-09', 3, 3200.00),
    (7, '2024-04-10', 1, 2200.00)
"""
cursor.execute(insert_data_query)

# Tạo bảng ChiTietPhieuNhap
create_table_query = """
    CREATE TABLE IF NOT EXISTS ChiTietPhieuNhap (
        MaChiTiet INT PRIMARY KEY,
        MaPhieuNhap INT NOT NULL,
        MaHangHoa NVARCHAR(5) NOT NULL,
        SoLuong INT NOT NULL,
        DonGia DECIMAL(18, 2) NOT NULL,
        FOREIGN KEY(MaPhieuNhap) REFERENCES PhieuNhap(MaPhieuNhap),
        FOREIGN KEY(MaHangHoa) REFERENCES HangHoa(MaHangHoa)
    )
"""
cursor.execute(create_table_query)

# Thêm dữ liệu vào bảng ChiTietPhieuNhap
insert_data_query = """
    INSERT INTO ChiTietPhieuNhap (MaChiTiet, MaPhieuNhap, MaHangHoa, SoLuong, DonGia) VALUES 
    (1, 1, 'HH1', 10, 100.00),
    (2, 2, 'HH2', 8, 150.00),
    (3, 3, 'HH3', 12, 200.00),
    (4, 4, 'HH4', 15, 120.00),
    (5, 5, 'HH5', 20, 180.00),
    (6, 6, 'HH6', 18, 220.00),
    (7, 7, 'HH7', 22, 130.00)
"""
cursor.execute(insert_data_query)
# truy vấn
cau1 =""
cursor.execute(
    "select * from hanghoa hh, nhacungcap ncc where hh.MaNhaCungCap = ncc.MaNhaCungCap and ncc.DiaChi = 'Trung Quốc'"
    )
c1 = cursor.fetchall()

for thamgia1 in c1:
    cau1 += f"{thamgia1}\n"
print("1. Hãy hiển thị danh sách các sản phẩm được cung cấp từ Trung Quốc là:\n", cau1)


cau2=""
cursor.execute(
    "select ncc.* from hanghoa hh, nhacungcap ncc ,loaihang lh where hh.MaNhaCungCap = ncc.MaNhaCungCap and lh.MaLoaiHang = hh.MaLoaiHang and lh.TenLoaiHang IN ('Tivi', 'Máy lạnh')"
    )
c2 = cursor.fetchall()

for thamgia2 in c2:
    cau2 += f"{thamgia2}\n"
print("2. Cho biết thông tin nhà cung cấp cung cấp Tivi và Máy lạnh là : \n", cau2)

cau3=""
cursor.execute(
    "select * from phieunhap where NgayNhap BETWEEN '2023-01-01' and '2023-06-30'"
    )
c3 = cursor.fetchall()

for phieu in c3:
    phieu_id, ngay_nhap, ma_nha_cung_cap, tong_tien = phieu
    formatted_ngay_nhap = ngay_nhap.strftime("%Y-%m-%d")
    formatted_tong_tien = "{:.2f}".format(tong_tien)
    cau3 += f"{phieu_id},{formatted_ngay_nhap},{ma_nha_cung_cap},{formatted_tong_tien}\n"

print("3. Cho biết thông tin các phiếu nhập sáu tháng đầu năm 2023 là:\n", cau3)


cau4=""
cursor.execute(
    "select TenNhaCungCap, DiaChi from nhacungcap where MaNhaCungCap NOT IN (SELECT DISTINCT MaNhaCungCap FROM phieunhap)"
    )
c4 = cursor.fetchall()

for thamgia4 in c4:
    cau4 += f"{thamgia4}\n"
print("4. Cho biết tên và địa chỉ của Nhà cung cấp chưa có phiếu nhập hàng nào. : \n", cau4)

cau5=""
cursor.execute(
    "SELECT * FROM nhacungcap ncc WHERE EXISTS ( SELECT 1 FROM hanghoa hh WHERE hh.MaNhaCungCap = ncc.MaNhaCungCap AND hh.MaLoaiHang IN ( SELECT MaLoaiHang FROM loaihang WHERE TenLoaiHang IN ('Tivi', 'Tủ lạnh')))"
    )
c5 = cursor.fetchall()

for thamgia5 in c5:
    cau5 += f"{thamgia5}\n"
print("5. Cho biết thông tin nhà cung cấp cung cấp Tivi hoặc tủ lạnh : \n", cau5)


cau6=""
cursor.execute(
    "SELECT * FROM nhacungcap ncc WHERE EXISTS (SELECT 1 FROM hanghoa hh WHERE hh.MaNhaCungCap = ncc.MaNhaCungCap GROUP BY hh.MaNhaCungCap HAVING COUNT(DISTINCT hh.MaLoaiHang) > 1 )"
    )
c6 = cursor.fetchall()

for thamgia6 in c6:
    cau6 += f"{thamgia6}\n"
print("6. Cho biết thông tin nhà cung cấp cung cấp nhiều hơn một loại mặt hàng : \n", cau6)
conn.commit()
conn.close()
