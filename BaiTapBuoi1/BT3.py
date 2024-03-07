n = int(input("Nhap so nguyen duong n: "))
result = ""

for i in range(1, n+1):
    if n % i == 0:
        result += str(i) + " "

print("Các ước số của n là : ",result.strip())
