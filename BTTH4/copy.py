class NhanVien:
    def __init__(self, hoten, namsinh, namcongtac):
        self.hoten = hoten
        self.namsinh = namsinh
        self.namcongtac = namcongtac
        

class ChuyenVien(NhanVien):
    def __init__(self, hoten, namsinh, namcongtac, trinhdo):
        super().__init__(hoten, namsinh, namcongtac)  
        self.trinhdo = trinhdo    
        self.bacluong = (namcongtac // 3) + 1

    def tongluong(self):
        if self.trinhdo == 'ĐH':
            return self.bacluong * 1000000
        elif self.trinhdo == 'CĐ':
            return self.bacluong * 800000
        elif self.trinhdo == 'TH':
            return self.bacluong * 500000

class CongNhan(NhanVien):
    def __init__(self, hoten, namsinh, namcongtac):
        super().__init__(hoten, namsinh, namcongtac)
        self.bacluong = (namcongtac // 3) + 1  

    def tongluong(self):
        return self.bacluong * 4000000  

lst_chuyenvien = []
print("Nhập vào số chuyên viên:", end=" ")
n = int(input())
while n <= 0:
    print("Nhập vào số chuyên viên:", end=" ")
    n = int(input())

for i in range(n):
    print("Nhập vào họ tên: ", end=" ")
    hoten = input()
    print("Nhập vào năm sinh: ", end=" ")
    namsinh = int(input())
    print("Nhập vào năm công tác: ", end=" ")
    namcongtac = float(input())
    print("Nhập vào trình độ (ĐH, CĐ, TH): ", end=" ")
    trinhdo = input()
    cv = ChuyenVien(hoten, namsinh, namcongtac, trinhdo)
    lst_chuyenvien.append(cv)

lst_congnhan = []

print("Nhập vào số công nhân:", end=" ")
m = int(input())
while m <= 0:
    print("Nhập vào số công nhân:", end=" ")
    m = int(input())

for i in range(m):
    print("Nhập vào họ tên: ", end=" ")
    hoten = input()
    print("Nhập vào năm sinh: ", end=" ")
    namsinh = int(input())
    print("Nhập vào năm công tác: ", end=" ")
    namcongtac = float(input())
    cn = CongNhan(hoten, namsinh, namcongtac)
    lst_congnhan.append(cn)

print(" Danh sách chuyên viên vừa nhập")    
print("{:<20}{:<20}{:<20}{:<20}{:<20}{:<20}".format("Họ tên", "Năm sinh", "Năm công tác", "Trình độ", "Bậc lương", "Lương"))
for i in range(n):
    print("{:<20}{:<20}{:<20}{:<20}{:<20}".\
          format(lst_chuyenvien[i].hoten, lst_chuyenvien[i].n
