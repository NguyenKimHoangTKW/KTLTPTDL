n = int(input("Nhập vào số n :"))
def TinhF(n):
    if n == 0:
        return 0
    else:
        return TinhF(n-1)+100
result = TinhF(n)
print(f"f{n} = {result}")