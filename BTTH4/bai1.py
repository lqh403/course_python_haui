# 1-	Tạo 1 class sinh viên chứa các thông tin Họ tên, Năm sinh,điểm toán, văn, ngoại ngữ. 
# Nhập 1 list sinh viên. Sắp xếp danh sách sinh viên theo thứ tự giảm dần của tổng điểm 3 môn. 
# Tính trung bình cộng  điểm toán, TBC điểm văn, TBC điểm ngoại ngữ của cả danh sách

class SinhVien:
    def __init__(self, hoten, namsinh, toan, van, nn):
        self.hoten = hoten
        self.namsinh = namsinh
        self.toan = toan
        self.van = van
        self.nn = nn
    def tongdiem(self):
        return self.toan + self.van + self.nn
    
lst_sv = []
print("Nhập vào số sinh viên:", end=" ")
n = int(input())
while n <= 0:
    print("Nhập vào số sinh viên:", end=" ")
    n = int(input())

for i in range(n):
    print("Nhập vào họ tên: ", end=" ")
    hoten = input()
    print("Nhập vào năm sinh: ", end=" ")
    namsinh = int(input())
    print("Nhập vào điểm toán: ", end=" ")
    toan = float(input())
    print("Nhập vào điểm văn: ", end=" ")
    van = float(input())
    print("Nhập vào điểm ngoại ngữ: ", end=" ")
    nn = float(input())

ob = SinhVien(hoten, namsinh, toan, van, nn)
lst_sv.append(ob)

print("Hiển thị danh sách sinh viên vừa nhập")    
print("{:<20}{:<20}{:<10}{:<10}{:<10}{:<20}".format("Họ tên", "Năm sinh", "Toán", "Văn", "Ngoại ngữ", "Tổng điểm"))

for i in range(n):
    print("{:<20}{:<20}{:<10}{:<10}{:<10}{:<20}".\
        format(lst_sv[i].hoten, lst_sv[i].namsinh, lst_sv[i].toan, lst_sv[i].van, lst_sv[i].nn, lst_sv[i].tongdiem()))





