# SGK/75
c = int(input("Tổng sản lượng cà phê: "))
a = int(input("Sản lượng Arabica: "))
if a / c >= 0.1:
    print("Arabica được mùa.")
    hs = 2
else:
    print("Arabica mất mùa.")
    hs = 3
print("Hệ số giá bán:", hs)

# SGK/76
n = int(input("Nhập n: "))
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0 and n % 400 != 0):
    if n % 3328 == 0:
        print("Năm nhuận kép.")
    else:
        print("Năm nhuận.")
else:
    print("Không phải là năm nhuận.")

# SGK/78
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
max = a
if max < b:
    max = b
if max < c:
    max = c
print("Max =", max)

# SGK/79
x = float(input("Nhập số điện tiêu thụ: "))
d1 = float(input("Nhập d1: "))
d2 = float(input("Nhập d2: "))
d3 = float(input("Nhập d3: "))
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if x <= a:
    t = x * d1
elif a < x <= b:
    t = a * d1 + (x - a) * d2
else:
    t = a * d1 + (b - a) * d2 + (x - b) * d3
print("Tiền điện là:", t)

# SGK/79
w = float(input("Cân nặng (kg): "))
h = float(input("Chiều cao (m): "))
BMI = w/h**2
if BMI < 18.5:
    print("Thiếu cân.")
elif BMI <= 22.9:
    print("Bình thường.")
else:
    print("Thừa cân.")