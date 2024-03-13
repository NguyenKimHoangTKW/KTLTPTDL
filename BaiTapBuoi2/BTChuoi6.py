numbers = [5, 6, 77, 45, 22, 12, 24]

ListXoaSoChan = [
    x for x in numbers 
    if x % 2 != 0
    ]

print(f"List sau khi loại bỏ các số chẵn: {ListXoaSoChan}")
