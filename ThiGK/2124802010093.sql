-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost:3306
-- Thời gian đã tạo: Th4 10, 2024 lúc 09:20 AM
-- Phiên bản máy phục vụ: 10.4.24-MariaDB
-- Phiên bản PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `quanlynhaphang`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `chitietphieunhap`
--

CREATE TABLE `chitietphieunhap` (
  `MaChiTiet` int(11) NOT NULL,
  `MaPhieuNhap` int(11) NOT NULL,
  `MaHangHoa` varchar(5) CHARACTER SET utf8 NOT NULL,
  `SoLuong` int(11) NOT NULL,
  `DonGia` decimal(18,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `chitietphieunhap`
--

INSERT INTO `chitietphieunhap` (`MaChiTiet`, `MaPhieuNhap`, `MaHangHoa`, `SoLuong`, `DonGia`) VALUES
(1, 1, 'HH1', 10, '100.00'),
(2, 2, 'HH2', 8, '150.00'),
(3, 3, 'HH3', 12, '200.00'),
(4, 4, 'HH4', 15, '120.00'),
(5, 5, 'HH5', 20, '180.00'),
(6, 6, 'HH6', 18, '220.00'),
(7, 7, 'HH7', 22, '130.00');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `hanghoa`
--

CREATE TABLE `hanghoa` (
  `MaHangHoa` varchar(5) CHARACTER SET utf8 NOT NULL,
  `TenHangHoa` varchar(60) CHARACTER SET utf8 NOT NULL,
  `MaNhaCungCap` int(11) NOT NULL,
  `MaLoaiHang` int(11) NOT NULL,
  `DonViTinh` varchar(20) CHARACTER SET utf8 NOT NULL,
  `DonGia` decimal(18,2) NOT NULL,
  `SoLuongTon` int(11) NOT NULL,
  `SoLuongDatHang` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `hanghoa`
--

INSERT INTO `hanghoa` (`MaHangHoa`, `TenHangHoa`, `MaNhaCungCap`, `MaLoaiHang`, `DonViTinh`, `DonGia`, `SoLuongTon`, `SoLuongDatHang`) VALUES
('HH1', 'Tivi Màu', 1, 1, 'Chiếc', '5.00', 50, 20),
('HH2', 'Máy lạnh Toshiba', 2, 2, 'Chiếc', '5.00', 30, 10),
('HH3', 'Tủ lạnh đẹp', 3, 3, 'Chiếc', '1000000.00', 40, 15),
('HH4', 'Bút đỏ hàng Limited', 5, 4, 'Cây', '20.00', 60, 25),
('HH5', 'Tẩy hàng Limited', 2, 5, 'Cục', '18.00', 35, 12),
('HH6', 'Bút xóa hàng Limited', 7, 6, 'Cây', '22.00', 45, 18),
('HH7', 'Tivi 42inch', 1, 7, 'Chiếc', '13000000.00', 55, 22);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `loaihang`
--

CREATE TABLE `loaihang` (
  `MaLoaiHang` int(11) NOT NULL,
  `TenLoaiHang` varchar(60) CHARACTER SET utf8 NOT NULL,
  `MoTa` varchar(100) CHARACTER SET utf8 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `loaihang`
--

INSERT INTO `loaihang` (`MaLoaiHang`, `TenLoaiHang`, `MoTa`) VALUES
(1, 'Tivi', NULL),
(2, 'Máy Lạnh', NULL),
(3, 'Tủ Lạnh', NULL),
(4, 'Bút đỏ', NULL),
(5, 'Cục tẩy', NULL),
(6, 'Bút Xóa', NULL),
(7, 'Tivi', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhacungcap`
--

CREATE TABLE `nhacungcap` (
  `MaNhaCungCap` int(11) NOT NULL,
  `TenNhaCungCap` varchar(30) CHARACTER SET utf8 NOT NULL,
  `TenNguoiLienLac` varchar(50) CHARACTER SET utf8 NOT NULL,
  `DiaChi` varchar(200) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `nhacungcap`
--

INSERT INTO `nhacungcap` (`MaNhaCungCap`, `TenNhaCungCap`, `TenNguoiLienLac`, `DiaChi`) VALUES
(1, 'Thanh Long', 'Nguyễn Kim Hoàng', 'Trung Quốc'),
(2, 'Bạch Hổ', 'Nguyễn Thành Long', 'Trung Quốc'),
(3, 'Chu Tước', 'Đào Thị Huỳnh Trang', 'Trung Quốc'),
(4, 'Huyền Vũ', 'Nguyễn Huỳnh Linh Đan', 'Việt Nam'),
(5, 'Dragon Ball', 'Đào Duy Tân', 'Nhật Bản'),
(6, 'Thiên Long', 'Huỳnh Thị Đào', 'Việt Nam'),
(7, 'Thiên Long Nhân', 'Đào Duy Thanh', 'Việt Nam');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `phieunhap`
--

CREATE TABLE `phieunhap` (
  `MaPhieuNhap` int(11) NOT NULL,
  `NgayNhap` datetime NOT NULL,
  `MaNhaCungCap` int(11) NOT NULL,
  `ThanhTien` decimal(18,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `phieunhap`
--

INSERT INTO `phieunhap` (`MaPhieuNhap`, `NgayNhap`, `MaNhaCungCap`, `ThanhTien`) VALUES
(1, '2023-04-10 00:00:00', 1, '2000.00'),
(2, '2023-04-11 00:00:00', 2, '2500.00'),
(3, '2023-04-12 00:00:00', 3, '3000.00'),
(4, '2023-04-07 00:00:00', 1, '2100.00'),
(5, '2023-04-08 00:00:00', 2, '2700.00'),
(6, '2024-04-09 00:00:00', 3, '3200.00'),
(7, '2024-04-10 00:00:00', 1, '2200.00');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `chitietphieunhap`
--
ALTER TABLE `chitietphieunhap`
  ADD PRIMARY KEY (`MaChiTiet`),
  ADD KEY `MaPhieuNhap` (`MaPhieuNhap`),
  ADD KEY `MaHangHoa` (`MaHangHoa`);

--
-- Chỉ mục cho bảng `hanghoa`
--
ALTER TABLE `hanghoa`
  ADD PRIMARY KEY (`MaHangHoa`),
  ADD KEY `MaNhaCungCap` (`MaNhaCungCap`),
  ADD KEY `MaLoaiHang` (`MaLoaiHang`);

--
-- Chỉ mục cho bảng `loaihang`
--
ALTER TABLE `loaihang`
  ADD PRIMARY KEY (`MaLoaiHang`);

--
-- Chỉ mục cho bảng `nhacungcap`
--
ALTER TABLE `nhacungcap`
  ADD PRIMARY KEY (`MaNhaCungCap`);

--
-- Chỉ mục cho bảng `phieunhap`
--
ALTER TABLE `phieunhap`
  ADD PRIMARY KEY (`MaPhieuNhap`),
  ADD KEY `MaNhaCungCap` (`MaNhaCungCap`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `chitietphieunhap`
--
ALTER TABLE `chitietphieunhap`
  ADD CONSTRAINT `chitietphieunhap_ibfk_1` FOREIGN KEY (`MaPhieuNhap`) REFERENCES `phieunhap` (`MaPhieuNhap`),
  ADD CONSTRAINT `chitietphieunhap_ibfk_2` FOREIGN KEY (`MaHangHoa`) REFERENCES `hanghoa` (`MaHangHoa`);

--
-- Các ràng buộc cho bảng `hanghoa`
--
ALTER TABLE `hanghoa`
  ADD CONSTRAINT `hanghoa_ibfk_1` FOREIGN KEY (`MaNhaCungCap`) REFERENCES `nhacungcap` (`MaNhaCungCap`),
  ADD CONSTRAINT `hanghoa_ibfk_2` FOREIGN KEY (`MaLoaiHang`) REFERENCES `loaihang` (`MaLoaiHang`);

--
-- Các ràng buộc cho bảng `phieunhap`
--
ALTER TABLE `phieunhap`
  ADD CONSTRAINT `phieunhap_ibfk_1` FOREIGN KEY (`MaNhaCungCap`) REFERENCES `nhacungcap` (`MaNhaCungCap`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
