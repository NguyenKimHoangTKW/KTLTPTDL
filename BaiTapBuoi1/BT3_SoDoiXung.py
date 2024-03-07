n = int(input("Hãy nhập vào số n :"))
KTdoixung =n
result = ""
while(n != 0):
    result += str(n % 10)
    n = n // 10
if(int(KTdoixung) == int(result)):
    print("là số đối xứng")