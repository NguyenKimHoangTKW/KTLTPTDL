result = ""
for i in range(10 , 200 + 1):
    if(i % 7 == 0 and i % 5 !=0):
        result += str(i) + ", "
print("Các số nằm trong đoạn từ 10 đến 200 chia hết cho 7 nhưng không chia hết cho 5 là :",result)