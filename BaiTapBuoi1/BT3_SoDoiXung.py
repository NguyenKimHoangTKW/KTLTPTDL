n = int(input("Hãy nhập vào số n :"))
KTdoixung =n
result = ""
while(n != 0):
    result += str(n % 10)
    n = n // 10
if(int(KTdoixung) == int(result)):
    print("Số",int(KTdoixung),"là số đối xứng")
else:
    print("Số ",int(KTdoixung), "không phải là số đối xứng")
    print("Vì đối số của",int(KTdoixung),"là số",int(result))