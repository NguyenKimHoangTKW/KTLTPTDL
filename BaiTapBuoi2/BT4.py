n = input("Nhập chuỗi cần lấy từ in đậm: ")
def TimVaInChuoiInDam(string):
    start_index = string.find('embed/') + len('embed/')
    end_index = string.find('?', start_index)
    if start_index == -1 or end_index == -1:
        return "Không tìm thấy đoạn in đậm trong chuỗi."
    bold_text = string[start_index:end_index]
    return bold_text
result = TimVaInChuoiInDam(n)
print(f"Đoạn in đậm trong chuỗi là : {result}")   