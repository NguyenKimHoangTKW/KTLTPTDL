string = input("Nhập vào dãy số cách nhau bằng dấu phẩy: ")
formatso = string.split(',')
tong = 0
result = " "
for i in formatso:
    tong += int(i)
    result += str(i) + ", "
print(f"Dãy số nhập vào là {result}")
print(f"Tổng của các số đã nhập là: {tong}")
