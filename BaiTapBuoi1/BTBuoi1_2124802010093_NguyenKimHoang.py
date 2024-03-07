# 1. viết chương trình nhập vào số m, tỉnh tổng các số chẵn từ 1 tới m, in ra tổng đó.
def TinhTongSoChan1denm():
    m = int(input("Nhập số m :"))
    result = ""
    tong = 0
    for i in range(1, m+1):
        if(i % 2 == 0):
            result += str(i) + " "
            tong += i
    print("Các số chẵn từ 1 tới m là :",result.strip())
    print("Tổng là :", tong)

# 2. Viết chương trình nhập vào số n, tính và in ra n!
def TinhnGiaiThua():
    n = int(input("Nhập số cần tính giai thừa: "))
    def giaithua(n):
        if n == 0:
            return 1
        return n * giaithua(n - 1)
    print ("Kết quả của giai thừa là :",giaithua(n))

# 3. Viết chương trình nhập vào số nguyên dương n, in ra tất cả các ước số của n
def InRaUocSoCuaN():
    n = int(input("Nhap so nguyen duong n: "))
    result = ""

    for i in range(1, n+1):
        if n % i == 0:
            result += str(i) + " "

    print("Các ước số của n là : ",result.strip())

# 4. Viết chương trình nhập vào số nguyên dương n, tỉnh tổng tất cả các ước số nguyên dương của n. Ví dụ nhập vào n = 6, thì các ước số nguyên dương của n là 1,2,3,6 => tống là 1+2+3+6=12.
def TinhTongUocSoNguyenDuong():
    n = int(input("Nhap so nguyen duong n: "))
    result = ""
    tong = 0
    for i in range(1, n+1):
        if (n % i == 0 and i > 0):
            result += str(i) + " "
            tong += i
    print("Các ước số của n là : ",result.strip())
    print("Tổng các ước số là : ",tong)

# 5. Viết chương trình tìm tất cả các số nằm trong đoạn 10 và 200 (tính có 10 và 200) chia hết cho 7 nhưng không chia hết cho 5
def SoChiaHet7KhongChiaHet5():
    result = ""
    for i in range(10 , 200 + 1):
        if(i % 7 == 0 and i % 5 !=0):
            result += str(i) + ", "
    print("Các số nằm trong đoạn từ 10 đến 200 chia hết cho 7 nhưng không chia hết cho 5 là :",result)

# 6. Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n Số nguyên dương n được nhập từ ban phim
def SoNguyenToNhoHonN():
    n = int(input("Nhap so nguyen duong n :"))
    result = ""
    for i in range(2,n):
        dem = 0
        for j in range(2,n):
            if i % j == 0:
                dem += 1
        if dem == 1:
            result += str(i) + " "
    print("Các số nguyên tố nhỏ hơn",n,"là:",result)

# 7. Viết chương trình cho phép nhập vào một số, kiểm tra xem số nhập vào có phải là số đối xứng hay không
def SoDoiXung():
    n = int(input("Hãy nhập vào số n :"))
    KTdoixung =n
    result = ""
    while(n != 0):
        result += str(n % 10)
        n = n // 10
    if(int(KTdoixung) == int(result)):
        print("Số",int(KTdoixung),"là số đối xứng")
    else:
        print("Số ",int(KTdoixung), "không phải là số đối xứng")
        print("Vì đối số của",int(KTdoixung),"là số",int(result))

# 8. Viết chương trình nhập vào hai chuỗi, in ra chuỗi có độ đại lớn hơn
def DoDaiChuoi():
    n = input(str("Nhập chuỗi 1: "))
    print(n)
    m = input(str("Nhập chuỗi 2: "))
    print(m)
    lenght1 = len(n)
    lenght2 = len(m)
    if(lenght1 > lenght2):
        print("Độ dài chuỗi 1 lớn hơn độ dài chuỗi 2")
    elif(lenght1 < lenght2):
        print("Độ dài chuỗi 2 lớn hơn độ dài chuỗi 1")
    else:
        print("Hai độ dài chuỗi bằng nhau")

# 9. Viết chương trình đoán số theo yêu cầu như sau Với một số đã có, người dùng nhập vào số để dự đoàn, nếu số dự đoán bằng với số đã có thì xuất thông báo "you win", ngược lại người dùng nhập lại (tối đa 3 lần) văn không đoán được thì in thông báo "you lose"
def SoLanThu():
    sodudoan = 10
    solanthu = 3

    for i in range(solanthu):
        n = int(input("Nhập số dự đoán của bạn: "))
        if n == sodudoan:
            print("you win")
            break
        else:
            print("you lose")
            print(f"Bạn còn {i+1}/3 lần thử.")
        if i == solanthu - 1:
            print(f"Bạn đã sử dụng hết {solanthu} lần thử, bạn đã thua hoàn toàn :)")


while True:
    print("MENU")
    print("Bài làm của sinh viên NGUYỄN KIM HOÀNG")
    print("----------------------------------------------------------------------------------")
    print("1. Tính tổng các số chẵn từ 1 đến m")
    print("2. Tính và in ra n!")
    print("3. In ra tất cả các ước số của n")
    print("4. Tính tổng các ước số nguyên dương của n")
    print("5. Tìm các số trong đoạn 10 dên 200 chia hết cho 7 nhưng không chia hết cho 5")
    print("6. Liệt kê số nguyên tố nhỏ hơn n")
    print("7. Kiểm tra số đối xứng")
    print("8. Kiểm tra và in ra chuỗi có độ dài lớn hơn")
    print("9. Nhập số và dự đoán số")
    print("Nhập 0 để kết thúc chương trình")
    print("----------------------------------------------------------------------------------")
    choice = input("Vui lòng chọn bài toán :")
    print("----------------------------------------------------------------------------------")
    if choice == "1":
        print("Bạn đã chọn Tính tổng các số chẵn từ 1 đến m")
        print("----------------------------------------------------------------------------------")
        TinhTongSoChan1denm()
        print("----------------------------------------------------------------------------------")
    elif choice == "2":
        print("Bạn đã chọn Tính và in ra n!")
        print("----------------------------------------------------------------------------------")
        TinhnGiaiThua()
        print("----------------------------------------------------------------------------------")
    elif choice == "3":
        print("Bạn đã chọn In ra tất cả các ước số của n")
        print("----------------------------------------------------------------------------------")
        InRaUocSoCuaN()
        print("----------------------------------------------------------------------------------")
    elif choice == "4":
        print("Bạn đã chọn Tính tổng các ước số nguyên dương của n")
        print("----------------------------------------------------------------------------------")
        TinhTongUocSoNguyenDuong()
        print("----------------------------------------------------------------------------------")
    elif choice == "5":
        print("Bạn đã chọn Tìm các số trong đoạn 10 dên 200 chia hết cho 7 nhưng không chia hết cho 5")
        print("----------------------------------------------------------------------------------")
        SoChiaHet7KhongChiaHet5()
        print("----------------------------------------------------------------------------------")
    elif choice == "6":
        print("Bạn đã chọn Liệt kê số nguyên tố nhỏ hơn n")
        print("----------------------------------------------------------------------------------")
        SoNguyenToNhoHonN()
        print("----------------------------------------------------------------------------------")
    elif choice == "7":
        print("Bạn đã chọn Kiểm tra số đối xứng")
        print("----------------------------------------------------------------------------------")
        SoDoiXung()
        print("----------------------------------------------------------------------------------")
    elif choice == "8":
        print("Bạn đã chọn Kiểm tra và in ra chuỗi có độ dài lớn hơn")
        print("----------------------------------------------------------------------------------")
        DoDaiChuoi()
        print("----------------------------------------------------------------------------------")
    elif choice == "9":
        print("Bạn đã chọn Nhập số và dự đoán số")
        print("----------------------------------------------------------------------------------")
        SoLanThu()
        print("----------------------------------------------------------------------------------")
    elif choice =="0":
        print("GoodBye")
        break
    else:
        print("Sai lựa chọn, vui lòng chọn lại")
