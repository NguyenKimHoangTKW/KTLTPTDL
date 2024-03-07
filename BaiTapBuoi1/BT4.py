n = int(input("Nhap so nguyen duong n: "))
result = ""
tong = 0
for i in range(1, n+1):
    if n % i == 0:
        result += str(i) + " "
        tong += i
print("Các ước số của n là : ",result.strip())
print("Tổng các ước số là : ",tong)

