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
