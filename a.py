#2.   Tạo 1 class nhân viên có các thông tin họ tên, năm sinh, năm công tác. 
#   Tạo class chuyên viên kế thừa từ lớp nhân viên có thêm các thông tin trình độ(ĐH, CĐ, TH), 
#   bậc lương được xác định từ số năm công tác(3 năm tăng 1 bậc, bắt đầu từ bậc 1). 
#   Tạo class công nhân kế thừa từ lớp nhân viên. 
#   Nhập danh sách chuyên viên, danh sách công nhân. 
#   Tính lương của mỗi nhân viên và tổng lương của cả 2 danh sách

class NhanVien:
    def __init__(self, hoten, namsinh, namcongtac):
        self.hoten = hoten
        self.namsinh = namsinh
        self.namcongtac = namcongtac

class ChuyenVien(NhanVien):
    def __init__(self, hoten, namsinh, namcongtac, trinhdo):
        super().__init__(hoten, namsinh, namcongtac)
        self.trinhdo = trinhdo
        self.bacluong = 1 + (namcongtac // 3)
    def tinh_luong(self):
        return self.bacluong * 50000000

class CongNhan(NhanVien):
    def __init__(self, hoten, namsinh, namcongtac):
        super().__init__(hoten, namsinh, namcongtac)
    def tinh_luong(self):
        self.bacluong = 1 + (self.namcongtac // 3)
        return self.bacluong * 40000000

def nhap_nhan_vien():
    hoten = input("Nhập họ tên: ")
    namsinh = int(input("Nhập năm sinh: "))
    namcongtac = int(input("Nhập năm công tác: "))
    return NhanVien(hoten, namsinh, namcongtac)



lst_chuyen_vien = []
lst_cong_nhan = []

print("Nhập danh sách chuyên viên:")
n = int(input("Nhập số lượng chuyên viên: "))
for i in range(n):
    print(f"Nhập thông tin chuyên viên thứ {i+1}")
    nhanvien = nhap_nhan_vien()
    trinhdo = input("Nhập trình độ: ")
    chuyenvien = ChuyenVien(nhanvien.hoten, nhanvien.namsinh, nhanvien.namcongtac, trinhdo)
    lst_chuyen_vien.append(chuyenvien)

print("Nhập danh sách công nhân:")
m = int(input("Nhập số lượng công nhân: "))
for j in range(m):
    print(f"Nhập thông tin công nhân thứ {j+1}")
    nhanvien = nhap_nhan_vien()
    cong_nhan = CongNhan(nhanvien.hoten, nhanvien.namsinh, nhanvien.namcongtac)
    lst_cong_nhan.append(cong_nhan)

# n = int(input("Nhập vào số chuyên viên: "))
# for i in range(n):
#     hoten = input("Nhập vào họ tên: ")
#     namsinh = int(input("Nhập vào năm sinh: "))
#     namcongtac = int(input("Nhập vào năm công tác: "))
#     trinhdo = input("Nhập vào trình độ: ")
#     ob = ChuyenVien(hoten, namsinh, namcongtac, trinhdo)
#     lst_chuyenvien.append(ob)

# m = int(input("Nhập vào số công nhân: "))
# for i in range(m):
#     hoten = input("Nhập vào họ tên: ")
#     namsinh = int(input("Nhập vào năm sinh: "))
#     namcongtac = int(input("Nhập vào năm công tác: "))
#     hesoluong = float(input("Nhập vào hệ số lương: "))
#     ob = CongNhan(hoten, namsinh, namcongtac, hesoluong)
#     lst_congnhan.append(ob)

print("Danh sách chuyên viên")
print("{:<20}{:<20}{:<20}{:<20}{:<20}".format("Họ tên", "Năm sinh", "Năm công tác", "Trình độ", "Lương"))

tong_luong = 0
for chuyenvien in lst_chuyen_vien:
    luong = chuyenvien.tinh_luong()
    tong_luong += luong
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".format(chuyenvien.hoten, chuyenvien.namsinh, chuyenvien.namcongtac, chuyenvien.trinhdo, luong))

print("Danh sách công nhân")
print("{:<20}{:<20}{:<20}{:<20}".format("Họ tên", "Năm sinh", "Năm công tác", "Lương"))

for congnhan in lst_cong_nhan:
    luong = congnhan.tinh_luong()
    tong_luong += luong
    print("{:<20}{:<20}{:<20}{:<20}".format(congnhan.hoten, congnhan.namsinh, congnhan.namcongtac, luong))

print("Tổng lương của cả 2 danh sách:", tong_luong)






