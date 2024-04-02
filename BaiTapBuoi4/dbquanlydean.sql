-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: localhost:3306
-- Thời gian đã tạo: Th3 27, 2024 lúc 10:33 AM
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
-- Cơ sở dữ liệu: `dbquanlydean`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `duan`
--

CREATE TABLE `duan` (
  `mada` int(11) NOT NULL,
  `tenda` varchar(255) DEFAULT NULL,
  `ngaybd` date DEFAULT NULL,
  `ngaykt` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `duan`
--

INSERT INTO `duan` (`mada`, `tenda`, `ngaybd`, `ngaykt`) VALUES
(1, 'Phần mềm quản lý trường học', '2018-02-02', '2020-07-05'),
(2, 'Hệ thống dự báo thời tiết', '2017-03-03', '2021-08-03'),
(3, 'Hệ thống xác thực vân tay', '2019-03-03', '2020-08-05'),
(4, 'Hệ thống nhận diện khuôn mặt', '2020-05-04', NULL);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `nhanvien`
--

CREATE TABLE `nhanvien` (
  `manv` int(11) NOT NULL,
  `tennv` varchar(255) NOT NULL,
  `tuoi` int(3) NOT NULL,
  `gioitinh` enum('0','1') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `nhanvien`
--

INSERT INTO `nhanvien` (`manv`, `tennv`, `tuoi`, `gioitinh`) VALUES
(1, 'Nguyễn Hoàng Oanh', 19, '0'),
(2, 'Trần Hạo Bình', 33, '1'),
(3, 'Bành Đại Kiện', 30, '1'),
(4, 'Quách Đại Lộ', 32, '1'),
(5, 'Hứa Thanh Hà', 24, '0');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `thamgia`
--

CREATE TABLE `thamgia` (
  `manv` int(11) NOT NULL,
  `mada` int(11) NOT NULL,
  `ngayvaoda` date DEFAULT NULL,
  `ngayradu` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `thamgia`
--

INSERT INTO `thamgia` (`manv`, `mada`, `ngayvaoda`, `ngayradu`) VALUES
(1, 1, '2018-03-03', '2019-05-07'),
(2, 1, '2018-02-02', '2020-05-05'),
(1, 2, '2017-03-03', '2019-05-05'),
(3, 2, '2019-03-03', '2021-04-04'),
(3, 3, '2019-03-03', '2020-04-04'),
(1, 4, '2020-05-04', NULL),
(2, 4, '2020-05-10', NULL);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `duan`
--
ALTER TABLE `duan`
  ADD PRIMARY KEY (`mada`);

--
-- Chỉ mục cho bảng `nhanvien`
--
ALTER TABLE `nhanvien`
  ADD PRIMARY KEY (`manv`);

--
-- Chỉ mục cho bảng `thamgia`
--
ALTER TABLE `thamgia`
  ADD KEY `mada_fk` (`mada`),
  ADD KEY `manv_fk` (`manv`);

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `thamgia`
--
ALTER TABLE `thamgia`
  ADD CONSTRAINT `mada_fk` FOREIGN KEY (`mada`) REFERENCES `duan` (`mada`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `manv_fk` FOREIGN KEY (`manv`) REFERENCES `nhanvien` (`manv`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
