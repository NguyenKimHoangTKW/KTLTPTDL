n = int(input("Nhập số n: "))
def generate_square_dict(n):
    square_dict = {}
    for i in range(1, n + 1):
        square_dict[i] = i * i
    return square_dict
result_dict = generate_square_dict(n)
print(f"Dãy số dictionart là {result_dict}")
