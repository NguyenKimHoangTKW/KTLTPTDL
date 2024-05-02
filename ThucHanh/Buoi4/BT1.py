from datetime import datetime

class Student:
    def __init__(self, TenHocSinh, NamSinh, TenPhuHuynh, SDT):
        self.TenHocSinh = TenHocSinh
        self.NamSinh = NamSinh
        self.TenPhuHuynh = TenPhuHuynh
        self.SDT = SDT

def Nhap_Thong_Tin_Hoc_Sinh():
    while True:
        TenHocSinh = input("Nhập tên học sinh: ")
        NamSinh = input("Nhập năm sinh học sinh: ")
        if not NamSinh.isdigit():
            print("Năm sinh phải là số.")
            continue
        elif int(NamSinh) <= 1900:
            print("Năm sinh phải lớn hơn 1900.")
            continue
        TenPhuHuynh = input("Nhập tên phụ huynh: ")
        SDT = input("Nhập số điện thoại: ")
        return Student(TenHocSinh, int(NamSinh), TenPhuHuynh, SDT)

def Cal_Tuoi(NamSinh):
    NamHienTai = datetime.now().year
    Tuoi = NamHienTai - int(NamSinh)
    return Tuoi

def Sap_Xep_Lop(students):
    for student in students:
        Tuoi = Cal_Tuoi(student.NamSinh)
        if Tuoi == 3:
            student.Lop = "Mầm"
        elif Tuoi == 4:
            student.Lop = "Chồi"
        elif Tuoi == 5:
            student.Lop = "Lá"
        elif Tuoi < 3:
            student.Lop = "Nhà trẻ"
        else:
            student.Lop = "Không xác định"
    return students

def main():
    students = []
    while True:
        print("\nChương trình quản lý học sinh")
        print("1. Nhập thông tin học sinh")
        print("2. Hiển thị danh sách học sinh")
        print("3. Số lượng học sinh lớp 'Nhà trẻ'")
        print("4. Thoát")
        choice = input("Chọn chức năng (1/2/3/4): ")
        if choice == '1':
            student = Nhap_Thong_Tin_Hoc_Sinh()
            students.append(student)
            Sap_Xep_Lop(students)
            print("Đã thêm học sinh vào danh sách.")
        elif choice == '2':
            if not students:
                print("Danh sách học sinh trống.")
            else:
                print("\nDanh sách học sinh:")
                print("STT  Tên học sinh    Tuổi        Lớp         Tên phụ huynh    Số điện thoại")
                for i, student in enumerate(students, 1):
                    ten_hocsinh = student.TenHocSinh.rjust(5).ljust(17)
                    tuoi = str(Cal_Tuoi(student.NamSinh)).ljust(8)
                    lop = student.Lop.ljust(17)
                    ten_phuhuynh = student.TenPhuHuynh.ljust(20)
                    sdt = student.SDT.ljust(15)
                    print(f"{i:<4}{ten_hocsinh}{tuoi}{lop}{ten_phuhuynh}{sdt}")
        elif choice == '3':
            count_nhatre = 0
            for student in students:
                if student.Lop == "Nhà trẻ":
                    count_nhatre += 1
            print(f"\nSố lượng học sinh lớp 'Nhà trẻ': {count_nhatre}")
            break
        elif choice == '4':
            with open("Hoc_Sinh.txt", "w", encoding="utf-8") as file:
                file.write("Tên học sinh        Tuổi        Lớp         Tên phụ huynh    Số điện thoại \n")
                for student in students:
                    ten_hocsinh = student.TenHocSinh.ljust(12)
                    tuoi = str(Cal_Tuoi(student.NamSinh)).ljust(9)
                    lop = student.Lop.ljust(13)
                    ten_phuhuynh = student.TenPhuHuynh.ljust(15)
                    sdt = student.SDT.ljust(15)
                    file.write(f"{ten_hocsinh}\t{tuoi}\t{lop}\t{ten_phuhuynh}\t{sdt}\n")
            print("Đã lưu học sinh vào file Hoc_Sinh.txt thành công")
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()