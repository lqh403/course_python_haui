class NhanVien:
    def __init__(self, hoten, namsinh, namcongtac):
        self.hoten = hoten
        self.namsinh = namsinh
        self.namcongtac = namcongtac

class ChuyenVien(NhanVien):
    def __init__(self, hoten, namsinh, namcongtac, trinhdo ):
        super().__init__(hoten, namsinh, namcongtac)  
        self.trinhdo = trinhdo    
        self.bacluong = (namcongtac // 3) + 1
    
    def tongluong(self):
        return self.trinhdo*100000000 
    


print("Nhập vào số nhân viên:", end=" ")
n = int(input())
while n <= 0:
    print("Nhập vào số nhân viên:", end=" ")
    n = int(input())

lst_chuyenvien = []
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

print("Danh sách chuyên viên vừa nhập")   
print("{:<20}{:<20}{:20}{:<20}{:<20}{:<20}".format("Họ tên", "Năm sinh", "Năm công tác", "Trình độ", "Bậc lương", "Lương"))
for i in range(n):

    print("{:<20}{:<20}{:<20}{:20}{:<20}{:<20}".\
          format(lst_chuyenvien[i].hoten, lst_chuyenvien[i].namsinh, lst_chuyenvien[i].namcongtac, lst_chuyenvien[i].trinhdo, lst_chuyenvien[i].bacluong, lst_chuyenvien[i].tongluong()))
