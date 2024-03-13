string = input("Nhập vào 1 chuỗi :")
def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str
  
print("Chuỗi nhập vào là : ", end="")
print(string)
  
print("Chuỗi đã được đảo ngược là : ", end="")
print(reverse(string))