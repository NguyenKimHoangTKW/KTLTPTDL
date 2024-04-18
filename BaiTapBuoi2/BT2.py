def Fibonaci(n):
    if(n >= 0):
        if n == 1 or n == 2:
            return 1
        elif n == 0:
            return 0
        else:
            return Fibonaci(n-1) + Fibonaci(n-2)
    else:
        print("Vui lòng nhập số >=0 ")
n = int(input("Nhap vao so n: "))
result = Fibonaci(n)
print(f"f{n} = {result}")