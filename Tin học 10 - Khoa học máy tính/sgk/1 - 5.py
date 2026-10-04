# SGK/52
help()
copyright()
credits()
license()

# SGK/61
a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
print(a + b + c)
print(a*a + b*b + c*c)

# SGK/63
day_ki_tu = input("Gõ vào ngày tháng năm sinh: ")
print("Ngày sinh:", day_ki_tu)

# SGK/64
a, b = 5, 3.2
print(type(a), type(b))

# SGK/66
van = float(input("Điểm Ngữ văn: "))
li = float(input("Điểm Vật lí: "))
sinh = float(input("Điểm Sinh học: "))
t = van + li + sinh
print("Tổng ba môn:", t, "trung bình:", t/3)

# SGK/70
from math import *
print(gcd(9855, 11556))
print(factorial(5))
print(ceil(16 / 3))