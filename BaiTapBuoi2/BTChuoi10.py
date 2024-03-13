phone_number = input("Nhập số điện thoại: ")
def ChuyenSoThanhChu(phone_number):
    anhxasovoichu = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    char_phone_number = [anhxasovoichu[digit] for digit in phone_number]
    print(' '.join(char_phone_number))
ChuyenSoThanhChu(phone_number)
