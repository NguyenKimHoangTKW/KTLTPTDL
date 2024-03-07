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