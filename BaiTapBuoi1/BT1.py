m = int(input("Nhập số m :"))
result = ""
tong = 0
for i in range(1, m+1):
    if(i % 2 == 0):
        result += str(i) + " "
        tong += i
print("Các số chẵn từ 1 tới m là :",result.strip())
print("Tổng là :", tong)