# 1. Viết hàm tính tông từ 1 tới n với n được nhập vào từ bàn phim
def InTongTu1denN():
    n = int(input("Nhap vao so n: "))
    def TinhTong(n):
        tong = 0
        for i in range(1, n+1):
            tong += i
        return tong
    tong = TinhTong(n)
    print(f"Các số từ 1 đến {n} là:", end=" ")
    for i in range(1, n+1):
        print(i, end=" ")
    print()
    print(f"Tổng của các số từ 1 đến {n} là {tong}")


# 2.Tình dây số Fibonaci theo công thức
def TinhDaySoFibonaci():
    n = int(input("Nhap vao so n: "))
    def Fibonaci(n):
        if(n >= 0):
            if n == 1 or n == 2:
                return 1
            elif n == 0:
                return 0
            else:
                return Fibonaci(n-1) + Fibonaci(n-2)
        else:
            print("Vui lòng nhập số >=0 ")
    result = Fibonaci(n)
    print(f"f{n} = {result}")

# 3. Viết chương trình tinhf(n) = f(n - 1) + 100 khi n > 0 khi n = 0 thì f(0) = 0 với n là số được nhập vào (n >= 0)
def TinhFn():
    n = int(input("Nhập vào số n :"))
    def TinhF(n):
        if n == 0:
            return 0
        else:
            return TinhF(n-1)+100
    result = TinhF(n)
    print(f"f{n} = {result}")

# 4. cho string  'https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent‘ cắt lấy phần chữ in đậm trong string trên.
def InRaChuoiInDam():
    string = 'https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent'
    start_index = string.find('embed/') + len('embed/')
    end_index = string.find('?', start_index)
    bold_text = string[start_index:end_index]
    print(f"Đoạn in đậm trong chuỗi là : {bold_text}")

def ChuoiDaoNguoc():
    string = input("Nhập vào 1 chuỗi :")
    def reverse(string):
        str = ""
        for i in string:
            str = i + str
        return str
    print("Chuỗi nhập vào là : ", end="")
    print(string)
  
    print("Chuỗi đã được đảo ngược là : ", end="")
    print(reverse(string))

def SoSanhDoDaiChuoi():
    n = input(str("Nhập chuỗi 1: "))
    print(n)
    m = input(str("Nhập chuỗi 1: "))
    print(m)
    lenght1 = len(n)
    lenght2 = len(m)
    if(lenght1 > lenght2):
        print(f"Độ dài chuỗi {n} của chuỗi 1 lớn hơn độ dài chuỗi 2 {m}")
    elif(lenght1 < lenght2):
        print(f"Độ dài chuỗi {m} của chuỗi 2 lớn hơn độ dài chuỗi 1 {n}")
    else:
        print("Hai độ dài chuỗi bằng nhau")

def TongDaySoNganCachBangDauPhay():
    string = input("Nhập vào dãy số cách nhau bằng dấu phẩy: ")
    formatso = string.split(',')
    tong = 0
    result = " "
    for i in formatso:
        tong += int(i)
        result += str(i) + ", "
    print(f"Dãy số nhập vào là {result}")
    print(f"Tổng của các số đã nhập là: {tong}")

def InHoaChuoi():
    string = input("Nhập chuỗi cần chuyển :")
    print(string.upper())

def DoDaiChuoiTrung():
    string = input("Nhập vào chuỗi: ")
    LoaiChuoiTrung= ''.join(sorted(set(string), key=string.index))
    print(f"len({string}) = ", len(LoaiChuoiTrung))

def LoaiBoSoChan():
    numbers = [5, 6, 77, 45, 22, 12, 24]
    ListXoaSoChan = [
        x for x in numbers 
        if x % 2 != 0
        ]

    print(f"List sau khi loại bỏ các số chẵn: {ListXoaSoChan}")

def LoaiBoSoChia5Va7():
    numbers = [12, 24, 35, 70, 88, 120, 155]
    ListSoLoaiBo = [
        x for x in numbers 
        if x % 5 != 0 and x % 7 != 0
        ]

    print(f"List sau khi loại bỏ số chia hết cho 5 và 7 là : {ListSoLoaiBo}")

def LoaiBoSoViTri0246():
    numbers = [12, 24, 35, 70, 88, 120, 155]

    ListSoLoaiBo = numbers[1:7:2]

    print("List sau khi loại bỏ các số ở vị trí 0, 2, 4 và 6:", ListSoLoaiBo)

def LoaiBoVaSapXepChuoi():
    string = input("Nhập vào chuỗi: ")
    def LoaiBoVaSapXepChuoi(sentence):
        words = list(set(sentence.split()))
        sorted_words = sorted(words)
        sorted_sentence = ' '.join(sorted_words)
        print("Các từ sau khi loại bỏ từ trùng lặp và sắp xếp là:", sorted_sentence)
    LoaiBoVaSapXepChuoi(string)

def NhapVaInRaSoDienThoaiDangKyTu():
    phone_number = input("Nhập số điện thoại: ")
    def ChuyenSoThanhChu(phone_number):
        anhxasovoichu = {
            '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
            '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
        }
        char_phone_number = [anhxasovoichu[digit] for digit in phone_number]
        print(' '.join(char_phone_number))
    ChuyenSoThanhChu(phone_number)

def InRaDictionary():
    n = int(input("Nhập số n: "))
    def generate_square_dict(n):
        square_dict = {}
        for i in range(1, n + 1):
            square_dict[i] = i * i
        return square_dict
    result_dict = generate_square_dict(n)
    print(f"Dãy số dictionart là {result_dict}")

def InRaViTriBatDauVaDich():
    def searchRange(nums, target):
        def search(nums, target, left):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] > target or (left and target == nums[mid]):
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        left_idx = search(nums, target, True)

        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, search(nums, target, False) - 1]
    nums1 = [5, 7, 7, 8, 8, 10]
    target1 = 8
    print(f"Dãy nhận vào là {nums1}")
    print(f"Đích : {target1}")
    print("Ví trí bắt đầu và kết thúc của giá trị đích là : ",searchRange(nums1, target1))

    nums2 = [5, 7, 7, 8, 8, 10]
    target2 = 6
    print(f"Dãy nhận vào là {nums2}")
    print(f"Đích : {target2}")
    print("Ví trí bắt đầu và kết thúc của giá trị đích là : ",searchRange(nums2, target2))

    nums3 = []
    target3 = 0
    print(f"Dãy nhận vào là {nums3}")
    print(f"Đích : {target3}")
    print("Ví trí bắt đầu và kết thúc của giá trị đích là : ",searchRange(nums3, target3))


while True:
    print("MENU")
    print("Bài làm Buổi 2 của sinh viên NGUYỄN KIM HOÀNG")
    print("----------------------------------------------------------------------------------")
    print("1. Tính tổng các số từ 1 đến n")
    print("2. Tính dãy số Finabonci")
    print("3. Tính F(n)")
    print("4. In ra chuỗi in đậm")
    print("5. Nhập và in ra chuỗi đảo ngược")
    print("6. Nhập vào 2 chuỗi và so sánh độ dài 2 chuỗi")
    print("7. Nhập và in ra tổng dãy số ngăn cách bằng dấu phẩy")
    print("8. Nhập và in hoa chuỗi")
    print("9. Nhập,kiểm tra và in ra độ dài chuỗi đã loại bỏ trùng nhau")
    print("10. In ra dãy số sau khi loại bỏ số chia hết cho 2")
    print("11. In ra dãy số sau khi loại bỏ số chia hết cho 5 và 7")
    print("12. In ra dãy số sau khi loại bỏ số ở vị trí 0,2,4,6")
    print("13. Loại bỏ và sắp xếp chuỗi trùng. In ra chuỗi hoàn thiện")
    print("14. Nhập và chuyển đổi số điện thoại thành ký tự")
    print("15. Nhập số và in ra dãy Dictionary")
    print("16. Tìm và in ra vị trí bắt đầu và đích với đích cho trước")
    print("Nhập 0 để kết thúc chương trình")
    print("----------------------------------------------------------------------------------")
    choice = input("Vui lòng chọn bài toán :")
    print("----------------------------------------------------------------------------------")
    if choice == "1":
        print("Bạn đã chọn Tính tổng các số từ 1 đến n")
        print("----------------------------------------------------------------------------------")
        InTongTu1denN()
        print("----------------------------------------------------------------------------------")
    elif choice == "2":
        print("Bạn đã chọn Tính dãy số Finabonci")
        print("----------------------------------------------------------------------------------")
        TinhDaySoFibonaci()
        print("----------------------------------------------------------------------------------")
    elif choice == "3":
        print("Bạn đã chọn Tính F(n)")
        print("----------------------------------------------------------------------------------")
        TinhFn()
        print("----------------------------------------------------------------------------------")
    elif choice == "4":
        print("Bạn đã chọn In ra chuỗi in đậm")
        print("----------------------------------------------------------------------------------")
        InRaChuoiInDam()
        print("----------------------------------------------------------------------------------")
    elif choice == "5":
        print("Bạn đã chọn Nhập và in ra chuỗi đảo ngược")
        print("----------------------------------------------------------------------------------")
        ChuoiDaoNguoc()
        print("----------------------------------------------------------------------------------")
    elif choice == "6":
        print("Bạn đã chọn Nhập vào 2 chuỗi và so sánh độ dài 2 chuỗi")
        print("----------------------------------------------------------------------------------")
        SoSanhDoDaiChuoi()
        print("----------------------------------------------------------------------------------")
    elif choice == "7":
        print("Bạn đã chọn Nhập và in ra tổng dãy số ngăn cách bằng dấu phẩy")
        print("----------------------------------------------------------------------------------")
        TongDaySoNganCachBangDauPhay()
        print("----------------------------------------------------------------------------------")
    elif choice == "8":
        print("Bạn đã chọn Nhập và in hoa chuỗi")
        print("----------------------------------------------------------------------------------")
        InHoaChuoi()
        print("----------------------------------------------------------------------------------")
    elif choice == "9":
        print("Bạn đã chọn Nhập,kiểm tra và in ra độ dài chuỗi đã loại bỏ trùng nhau")
        print("----------------------------------------------------------------------------------")
        DoDaiChuoiTrung()
        print("----------------------------------------------------------------------------------")
    elif choice == "10":
        print("Bạn đã chọn In ra dãy số sau khi loại bỏ số chia hết cho 2")
        print("----------------------------------------------------------------------------------")
        LoaiBoSoChan()
        print("----------------------------------------------------------------------------------")
    elif choice == "11":
        print("Bạn đã chọn In ra dãy số sau khi loại bỏ số chia hết cho 5 và 7")
        print("----------------------------------------------------------------------------------")
        LoaiBoSoChia5Va7()
        print("----------------------------------------------------------------------------------")
    elif choice == "12":
        print("Bạn đã chọn In ra dãy số sau khi loại bỏ số ở vị trí 0,2,4,6")
        print("----------------------------------------------------------------------------------")
        LoaiBoSoViTri0246()
        print("----------------------------------------------------------------------------------")
    elif choice == "13":
        print("Bạn đã chọn Loại bỏ và sắp xếp chuỗi trùng. In ra chuỗi hoàn thiện")
        print("----------------------------------------------------------------------------------")
        LoaiBoVaSapXepChuoi()
        print("----------------------------------------------------------------------------------")
    elif choice == "14":
        print("Bạn đã chọn Nhập và chuyển đổi số điện thoại thành ký tự")
        print("----------------------------------------------------------------------------------")
        NhapVaInRaSoDienThoaiDangKyTu()
        print("----------------------------------------------------------------------------------")
    elif choice == "15":
        print("Bạn đã chọn Nhập số và in ra dãy Dictionary")
        print("----------------------------------------------------------------------------------")
        InRaDictionary()
        print("----------------------------------------------------------------------------------")
    elif choice == "16":
        print("Bạn đã chọn Tìm và in ra vị trí bắt đầu và đích với đích cho trước")
        print("----------------------------------------------------------------------------------")
        InRaViTriBatDauVaDich()
        print("----------------------------------------------------------------------------------")
    elif choice =="0":
        print("GoodBye")
        break
    else:
        print("Sai lựa chọn, vui lòng chọn lại từ 1 đến 16")