import requests
from bs4 import BeautifulSoup
import csv


#1
def ChuyenSDTThanhChu():
    phone_number = input("Nhập số điện thoại: ")
    def ChuyenSoThanhChu(phone_number):
        anhxasovoichu = {
            '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
        }
        char_phone_number = [anhxasovoichu[digit] for digit in phone_number]
        print(' '.join(char_phone_number))
    ChuyenSoThanhChu(phone_number)
#2
def NhapVaInDayDi():
    n = int(input("Nhập số n: "))
    def generate_square_dict(n):
        square_dict = {}
        for i in range(1, n + 1):
            square_dict[i] = i * i
        return square_dict
    result_dict = generate_square_dict(n)
    print(f"Dãy số dictionart là {result_dict}")       
#3
def TaoVaInraGTBinhPhuong():
    n = int(input("Nhập vào số n: "))
    squared_list = []
    for i in range(1, n + 1):
        squared_list.append(i ** 2)
        print(squared_list)
#4
def TaoVaInRaTupleInRaGTBinhDuong():
    n = int(input("Nhập vào số n: "))
    squared_tuple = tuple(i ** 2 for i in range(1, n + 1))
    print(squared_tuple)
#5
def TaoVaInRaTupleSoChan():
    so_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    SoChan_tuple = tuple(num for num in so_tuple if num % 2 == 0)
    print(SoChan_tuple)

#6
def ListPhanTuGiao():
    list1 = [1, 3, 6, 78, 35, 55, 88, 120]
    list2 = [12, 24, 35, 24, 88, 120, 155]
    ListGiaoNhau = list(set(list1) & set(list2))
    print(ListGiaoNhau)
#7
def XoaGiaTriTrung():
    list_phantu = [1, 3, 6, 78, 35, 55, 88, 120, 12, 24, 35, 24, 88, 120, 155]
    XoaPhanTuTrung = set(list_phantu)
    TaoListMoiDaXoa = list(XoaPhanTuTrung)
    print(TaoListMoiDaXoa)
#8
def ChuaGiaTriTrung():
    original_list = [1, 3, 6, 78, 35, 55, 88, 120, 12, 24, 35, 24, 88, 120, 155]
    duplicate_values = []
    seen = set()
    for value in original_list:
        if original_list.count(value) > 1 and value not in seen:
            duplicate_values.append(value)
            seen.add(value)
    print(duplicate_values)
#9
def SingleNumber1():
    def singleNumber(nums):
        result = 0
        for num in nums:
            result ^= num
        return result
    nums1 = [2, 2, 1]
    print(singleNumber(nums1)) 
    nums2 = [4, 1, 2, 1, 2]
    print(singleNumber(nums2)) 
    nums3 = [1]
    print(singleNumber(nums3)) 
#10
def SingleNumber2():
    def singleNumber(nums):
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            result |= (count % 3) << i
        if result >= 2**31:
            result -= 2**32
        return result

    nums1 = [2, 2, 3, 2]
    print(singleNumber(nums1)) 

    nums2 = [0, 1, 0, 1, 0, 1, 99]
    print(singleNumber(nums2))
# In Sách
def inRa1000BookSach():
    with open('booktoscrape_2124802010093.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["ID",'Book', 'Price'])
        number = 0
        for page in range(1, 51):
            url = f"https://books.toscrape.com/catalogue/page-{page}.html"
            resp = requests.get(url)
            soup = BeautifulSoup(resp.content, "html.parser")
            parents = soup.find_all("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})
            for parent in parents:
                    number += 1
                    element = parent.find("h3")
                    result = element.find("a")
                    book = result["title"]
                    price = parent.find("p", {"class": "price_color"}).get_text()
                    format_price = price.replace("£", "$")
                    print([number,book, format_price])
                    writer.writerow([number,book, format_price])
while True:
    print("MENU")
    print("Bài làm Buổi 3 của sinh viên NGUYỄN KIM HOÀNG")
    print("----------------------------------------------------------------------------------")
    print("1. Nhập và chuyển đổi số điện thoại thành ký tự")
    print("2. Nhập số và in ra dãy Dictionary")
    print("3. Tạo và in ra list chứa bình phương từ 1 đến n")
    print("4. Tạo và in ra tuple chứa bình phương từ 1 đến n")
    print("5. Tạo và in ra tuple chứa các số chẵn được lấy từ tuple")
    print("6. Tạo list có phần tử là giao của 2 list đã cho")
    print("7. Tạo list sau khi xóa giá trị trùng")
    print("8. Tạo list chứa các giá trị trùng")
    print("9. SingleNumber1")
    print("10. SingleNumber2")
    print("11. In ra 1000 sách từ web BookToScapre và in vào file csv")
    print("Nhập 0 để kết thúc chương trình")
    print("----------------------------------------------------------------------------------")
    choice = input("Vui lòng chọn bài toán :")
    print("----------------------------------------------------------------------------------")
    if choice == "1":
        print("Bạn đã chọn Nhập và chuyển đổi số điện thoại thành ký tự")
        print("----------------------------------------------------------------------------------")
        ChuyenSDTThanhChu()
        print("----------------------------------------------------------------------------------")
    elif choice == "2":
        print("Bạn đã chọn Nhập số và in ra dãy Dictionary")
        print("----------------------------------------------------------------------------------")
        NhapVaInDayDi()
        print("----------------------------------------------------------------------------------")
    elif choice == "3":
        print("Bạn đã chọn Tạo và in ra list chứa bình phương từ 1 đến n")
        print("----------------------------------------------------------------------------------")
        TaoVaInraGTBinhPhuong()
        print("----------------------------------------------------------------------------------")
    elif choice == "4":
        print("Bạn đã chọn Tạo và in ra tuple chứa bình phương từ 1 đến n")
        print("----------------------------------------------------------------------------------")
        TaoVaInRaTupleInRaGTBinhDuong()
        print("----------------------------------------------------------------------------------")
    elif choice == "5":
        print("Bạn đã chọn Tạo và in ra tuple chứa các số chẵn được lấy từ tuple")
        print("----------------------------------------------------------------------------------")
        TaoVaInRaTupleSoChan()
        print("----------------------------------------------------------------------------------")
    elif choice == "6":
        print("Bạn đã chọn Tạo list có phần tử là giao của 2 list đã cho")
        print("----------------------------------------------------------------------------------")
        ListPhanTuGiao()
        print("----------------------------------------------------------------------------------")
    elif choice == "7":
        print("Bạn đã chọn Tạo list sau khi xóa giá trị trùng")
        print("----------------------------------------------------------------------------------")
        XoaGiaTriTrung()
        print("----------------------------------------------------------------------------------")
    elif choice == "8":
        print("Bạn đã chọn Tạo list chứa các giá trị trùng")
        print("----------------------------------------------------------------------------------")
        ChuaGiaTriTrung()
        print("----------------------------------------------------------------------------------")
    elif choice == "9":
        print("Bạn đã chọn SingleNumber1")
        print("----------------------------------------------------------------------------------")
        SingleNumber1()
        print("----------------------------------------------------------------------------------")
    elif choice == "10":
        print("Bạn đã chọn SingleNumber2")
        print("----------------------------------------------------------------------------------")
        SingleNumber2()
        print("----------------------------------------------------------------------------------")
    elif choice == "11":
        print("Bạn đã chọn In ra 1000 sách từ web BookToScapre và in vào file csv")
        print("----------------------------------------------------------------------------------")
        inRa1000BookSach()
        print("----------------------------------------------------------------------------------")
    elif choice =="0":
        print("GoodBye")
        break
    else:
        print("Sai lựa chọn, vui lòng chọn lại từ 1 đến 16")