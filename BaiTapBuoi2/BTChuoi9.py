string = input("Nhập vào chuỗi: ")
def LoaiBoVaSapXepChuoi(sentence):
    words = list(set(sentence.split()))
    sorted_words = sorted(words)
    sorted_sentence = ' '.join(sorted_words)
    print("Các từ sau khi loại bỏ từ trùng lặp và sắp xếp là:", sorted_sentence)

LoaiBoVaSapXepChuoi(string)
