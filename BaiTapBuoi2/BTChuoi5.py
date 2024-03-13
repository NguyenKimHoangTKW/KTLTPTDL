string = input("Nhập vào chuỗi: ")
LoaiChuoiTrung= ''.join(sorted(set(string), key=string.index))
print(f"len({string}) = ", len(LoaiChuoiTrung))
