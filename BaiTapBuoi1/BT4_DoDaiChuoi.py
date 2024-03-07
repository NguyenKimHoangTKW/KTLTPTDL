n = input(str("Nhập chuỗi 1: "))
print(n)
m = input(str("Nhập chuỗi 1: "))
print(m)
lenght1 = len(n)
lenght2 = len(m)
if(lenght1 > lenght2):
    print("Độ dài chuỗi 1 lớn hơn độ dài chuỗi 2")
elif(lenght1 < lenght2):
    print("Độ dài chuỗi 2 lớn hơn độ dài chuỗi 1")
else:
    print("Hai độ dài chuỗi bằng nhau")
