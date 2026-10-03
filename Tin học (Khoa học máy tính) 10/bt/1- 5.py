# F5
h, m, s = 2, 28, 9
print(h * 3600 + m * 60 + s)

# F6
avg_age, dad_age, mom_age, sis_age = 25, 40, 38, 8
print(avg_age * 4 - (dad_age + mom_age + sis_age))

# F7
l, w, S = 37, 10, 100
print((l * w - S) / 3)

# F8
print(max(22**21, 21**22))

# F9
n = 5
sum = (n * (n + 1) * (n + 2) * (2*n + 1)) / 6
print(sum)

# F10
t = 28
length = (t  - 1) * 50
print(length)

# F11
a, b, c = 600, 700, 300
t = (a + b + c) / 2
print("An:", t - b)
print("Bình:", t - c)
print("Cường:", t - a)

# F13
a, b = 2, 1
num = (a*10 + b*10)  * 2/5
print(num)

# F14
d, s = 307, 10
print(d//s, d%s)

# F15
a, b = int(input("a = ")), int(input("b = "))
t = 1 / (1/a + 1/b)
print(t)

# F16
a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
t = 1 / (1/a + 1/b + 1/c)
print(t)

# F17
t, v, d = 15, 80, 100
p = (t * v) / 2
a, b = (p + d) / 2, (p - d) / 2
print("Chiều dài:", a)
print("Chiều rộng:", b)

# F18
A, B, C = float(input()), float(input()), float(input())
delta = B*B - 4*A*C
x1, x2 = (-B + delta**(1/2)) / (2*A), (-B - delta**(1/2)) / (2*A)
print(x1, x2)

# F19
x = float(input("x = "))
print("Phần nguyên:", x)
print("Phần thập phân:", x - int(x))

# F20
n = int(input("n = "))
print(n - n // 18)

# F21
a, b = float(input("a = ")), float(input("b = "))
A, B, C = (a * b) / 2, ((100 - a) * 100) / 2, ((100 - b) * 100) / 2
print(100*100 - A - B - C)

# F22
x, y = int(input("x = ")), int(input("y = "))
print("Tổng số vé:", x + y)
print("Tổng số tiền:", x*500 + y*300)

# F23
n = int(input("n = "))
print("Số cách chọn:", n*(n - 1))

# F24
a, b = int(input()), int(input())
print("Số cách chọn:", a * b)

# F25
d, m = int(input("d = ")), int(input("m = "))
print("Kết quả:", (d//m) + 1)

# F26
a = int(input("a = "))
S = 3.14 * (a / 2)**2
print((a*a - S) / 4)