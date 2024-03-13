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
