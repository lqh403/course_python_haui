#2.	Tạo 1 class nhân viên có các thông tin họ tên, năm sinh, năm công tác. 
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
        self.bacluong = (namcongtac // 3) + 1

    def tongluong(self):
        return self.trinhdo*100000000   

   
class CongNhan(NhanVien):
    def __init__(self, hoten, namsinh, namcongtac):
        super().__init__(hoten, namsinh, namcongtac)
        self.bacluong = (namcongtac // 3) + 1              
       

lst_chuyenvien = []
print("Nhập vào số nhân viên:", end=" ")
n = int(input())
while n <= 0:
    print("Nhập vào số nhân viên:", end=" ")
    n = int(input())

for i in range(n):
    print("Nhập vào họ tên: ", end=" ")
    hoten = input()
    print("Nhập vào năm sinh: ", end=" ")
    namsinh = int(input())
    print("Nhập vào năm công tác: ", end=" ")
    namcongtac = float(input())
    print("Nhập vào trình độ : ", end=" ")
    trinhdo = str(input())
    print("_________________")  
    cv = ChuyenVien(hoten, namsinh, namcongtac, trinhdo )
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
    print("_________________")  
    cn = CongNhan(hoten, namsinh, namcongtac)
    lst_congnhan.append(cn)

print("Danh sách chuyên viên vừa nhập")    
print("{:<20}{:<20}{:20}{:<20}{:<20}{:<20}".format("Họ tên", "Năm sinh", "Năm công tác", "Trình độ", "Bậc lương", "Lương"))
for i in range(n):
    print("{:<20}{:<20}{:20}{:<20}{:<20}".\
          format(lst_chuyenvien[i].hoten, lst_chuyenvien[i].namsinh, lst_chuyenvien[i].namcongtac, lst_chuyenvien[i].trinhdo, lst_chuyenvien[i].bacluong, lst_chuyenvien[i].tongluong()))





print("Danh sách công nhân vừa nhập") 
print("{:<20}{:<20}{:<20}{:<20}".format("Họ tên", "Năm sinh", "Năm công tác", "Bậc lương"))

for i in range(m):
    print("{:<20}{:<20}{:<20}{:<20}".\
          format(lst_congnhan[i].hoten, lst_congnhan[i].namsinh, lst_congnhan[i].namcongtac, lst_congnhan[i].bacluong))