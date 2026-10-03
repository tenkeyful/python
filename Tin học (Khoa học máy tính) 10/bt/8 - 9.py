# F35
n = int(input("n  = "))
# Cách 1:
x = 1
while x <= n:
    print(x)
    x += 2
# Cách 2:
for k in range((n - 1) // 2 + 1):
    print(k * 2 + 1)
#Cách 3:
for k in range(1, n + 1, 2):
    print(k)

# F36
n = int(input("n = "))
# Cách 1:
x = n - n % 2
while x > 0:
    print(x)
    x -= 2
# Cách 2:
k = n // 2
for i in range(k): print((k - i) * 2)
# Cách 3:
for k in range(n - n % 2, 0, -2):
    print(k)

# F37
print("n =", end = " ")
n = int(input())
sum = 0
for i in range(1, n):
    if i % 3 == 0 or i % 5 == 0: sum += i
print("Sum =", sum)

# F38
print("Nhập lần lượt các số m, n (m < n) và b, mỗi số trên một dòng:")
m, n, b, sum = int(input()), int(input()), int(input()), 0
for i in range(m, n):
    if i % 3 == 0 or i % 5 == 0:
        if i % 15 != 0: sum += i
    if sum >= b: break
print("Sum =", sum)

# F39
p, d = int(input()), 0
while p <= 10**6:
    d += 1
    p *= 2
print("Số ngày:", d)

# F40
import math
a, b, sum= math.ceil(float(input())), math.floor(float(input())), 0
for x in range(a, b + 1): sum += x
print("Tổng:", sum)

# F41
n, S = int(input("n = ")), 0
while n != 0:
    d = n % 10
    S += d
    n //= 10
print("Tổng chữ số =", S)

# F42
n, F = int(input("n = ")), 1
for i in range(1, n + 1):
    F *= i
print(n, "!=", F)

# F43
a, b = int(input("a = ")), int(input("b = "))
# Cách 1:
if b == 0: d = a
else: d = b
while a % d != 0 or b % d != 0: d -= 1
print("GCD =", d)
# Cách 2: (Thuật toán Euclid)
while b != 0:
    a, b = b, a % b
print("GCD =", a)

# F44:
n = int(input("n = "))
# Cách 1:
for d in range(1, n + 1):
    if n % d == 0:
        print(d, end = " ")
# Cách 2:
d = 1
while d*d < n:
    if n % d == 0:
        print(d, n // d, end = " ")
        d += 1
    if d*d == n:
        print(d)