

class SinhVien:
    def __init__(self, hoten, namsinh, toan, van, nn):
        self.hoten = hoten
        self.namsinh = namsinh
        self.toan = toan
        self.van = van
        self.nn = nn
        
    def tongdiem(self):
        return self.toan + self.van + self.nn
    
n = int(input("Nhập vào số sinh viên: "))
while n <= 0:
    n = int(input("Nhập lại số sinh viên (số nguyên dương): "))

lst_sv = [SinhVien(input("Nhập họ tên: "),
                   int(input("Nhập năm sinh: ")),
                   float(input("Nhập điểm toán: ")),
                   float(input("Nhập điểm văn: ")),
                   float(input("Nhập điểm ngoại ngữ: ")))
          for i in range(n)]

lst_sv_sorted = sorted(lst_sv, key=lambda sv: sv.tongdiem(), reverse=True)

print("Danh sách sinh viên vừa nhập:")
print(f"{'Họ tên':<20} {'Năm sinh':<10} {'Điểm toán':<10} {'Điểm văn':<10} {'Điểm ngoại ngữ':<10} {'Tổng điểm':<10}")
for sv in lst_sv_sorted:
    print(f"{sv.hoten:<20} {sv.namsinh:<10} {sv.toan:<10} {sv.van:<10} {sv.nn:<10} {sv.tongdiem():<10}")

toan_avg = sum([sv.toan for sv in lst_sv]) / n
van_avg = sum([sv.van for sv in lst_sv]) / n
nn_avg = sum([sv.nn for sv in lst_sv]) / n

print(f"Điểm trung bình cộng toán của cả danh sách là: {toan_avg:.2f}")
print(f"Điểm trung bình cộng văn của cả danh sách là: {van_avg:.2f}")
print(f"Điểm trung bình cộng ngoại ngữ của cả danh sách là: {nn_avg:.2f}")
