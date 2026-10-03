# F27
x = float(input("x = "))
if x < 0: x = -x
print(x)

# F28
a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
if 2 * max(a, b, c) < a + b + c: print("Xếp được.")
else: print("Không xếp được.")

# F29
n, k = int(input("n = ")), int(input("k = "))
# Cách 1:
if n % k == 0: print("Số hộp =", n // k)
else: print("Số hộp =", n // k + 1)
# Cách 2:
print("Số hộp =", (n + k - 1) // k)

# F30
m, y = int(input("Tháng = ")), int(input("Năm = "))
if m == (4, 6, 9, 11):
    d = 30
elif m == 2:
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        d = 29
    else:
        d = 29
else:
    d = 31
print(f"Tháng {m} năm {y} có {d} ngày.")

# F31
s = int(input())
if s >= 373:
    print("Đạt Huy chương vàng.")
else:
    print("Không đạt Huy chương vàng.")

# F32
a, b, c = int(input()), int(input()), int(input())
if (a == b) and (a == c):
    print("Phương trình có một nghiệm duy nhất.")
elif (a != b) and (a != c) and (b != c):
    print("Phương trình có ba nghiệm phân biệt.")
else:
    print("Phương trình có hai nghiệm phân biệt.")

# F33
x, y = float(input("x = ")), float(input("y = "))
if x > 0 and y > 0: k = 1
elif x < 0 and y > 0: k = 2
elif x < 0 and y < 0: k = 3
else: k = 4
print("Điểm A thuộc góc phần tư thứ", k)

# F34
a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))
if a < b: a, b = b, a
elif a < c: a, c = c, a
elif b < c: b, c = c, b
print("Tốc độ gió tối đa là:", b)