my_list = [0,1,2,3,4,5,6,7,8,9]
sochan = " "
sole = " "
for i in my_list:
    if (i % 2 == 0):
        sochan += str(i) + " "
    else:
        sole += str(i) + " "
print(f"Dãy số chẵn trong my_list là : {sochan}")
print(f"Dãy số lẻ trong my_list là : {sole}")