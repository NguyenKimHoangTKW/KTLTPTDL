numbers = [12, 24, 35, 70, 88, 120, 155]

ListSoLoaiBo = [
    x for x in numbers 
    if x % 5 != 0 and x % 7 != 0
    ]

print(f"List sau khi loại bỏ số chia hết cho 5 và 7 là : {ListSoLoaiBo}")
