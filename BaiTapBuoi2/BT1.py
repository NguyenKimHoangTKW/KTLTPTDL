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
