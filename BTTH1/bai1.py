#1. Nhập 1 số nguyên từ bàn phím. Kiểm tra xem số vừa nhập là số chẵn hay số lẻ.


a = int(input("Mời nhập số: "))

if a % 2 == 0:
    print(f"Số {a} là số chẵn ")
else:
    print(f"Số {a} là số lẻ ")
    