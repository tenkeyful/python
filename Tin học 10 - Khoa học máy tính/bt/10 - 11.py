# F45
def divisors(n):
    res = 0
    k = int(n**0.5 + 0.5)
    for i in range(2, k + 1):
        if n % i == 0: res += 2
        elif i*i == n: res -= 1
    return res
m = int(input())
print(divisors(m))

# F46
def prime(n):
    if n == 2: return True
    elif n < 2 or n % 2 == 0: return False
    k = int(n**0.5 + 0.5)
    for i in range(3, k + 1, 2):
        if n % i == 0: return False
    return True
m = int(input())
print(prime(m))

# F47
def sum_digits(n):
    t = 0
    while n > 0:
        t += n % 10
        n //= 10
    return t
n = int(input())
print(sum_digits(n))

# F48
# Cách 1:
def g_prog(a, b, c): return a*a == b*c or b*b == a*c or c*c == a*b
x, y, z = map(float, input().split())
if g_prog(x, y, z): print("Yes")
else: print("No")
# Cách 2:
def g_prog(a, b, c):
    max_value = max(a, b, c)

    d1 = b - a
    d2 = c - b

    return d1 == d2

x, y, z = map(float, input().split())
if g_prog(x, y, z): print("Yes")
else: print("No")

# F49
# Cách 1:
def g_prog(a, b, c): return a*a == b*c or b*b == a*c or c*c == a*b
x, y, z = map(float, input().split())
if g_prog(x, y, z): print("Yes")
else: print("No")
# Cách 2:
def g_prog(a, b, c): return abs(b * c - a * c) < 1e-6
x, y, z = map(float, input().split())
if g_prog(x, y, z): print("Yes")
else: print("No")

# F50
def delay(a):
    return a * 3600 / 1_000_000
a = float(input())
print(round(delay(a) * 1700))

# F51
def Sum2(a, b, c):
    return a == b + c or b == a + c or c == a + b
a, b, c = map(int, input().split())
if Sum2(a, b, c): print("Yes")
else: print("No")

# F53
t, v = map(float, input().split())
def Feel_t(t, v):
    ft = t / (v*v)
print(Feel_t(t, v))

# F54 - Collatz conjecture
def Collatz(a):
    if a % 2 == 0: return a // 2
    else: return 3*a + 1

# F55
def factorial(n):
    t = 1
    for i in range(1, n + 1):
        t *= i
    return t
k = int(input("Số lượng test: "))
for i in range(k):
    n = int(input("n = "))
    print(n, "!=", factorial(n))

# F56
import math
def BCNN(x, y):
    return x * y / math.gcd(x, y)
n = int(input("n = "))
for i in range(n):
    s = input("a, b = ").split()
    a, b = int(s[0]), int(s[1])
    print("Bội chung nhỏ nhất:", BCNN(a, b), end = "\n")