# F57
s = input("s = ")
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(len(s))

# F58
s = input()
print(s[(len(s) + 1) // 2:] +s[: (len(s) + 1) // 2])

# F59
s = input()
for i in range(len(s)):
    if i % 2 == 0:
        s = s.replace(s[i], "*")
print(s)

# F60
s, c = input(), input()
if s.count(c) == 1:
    print(s.find(c))
elif s.count(c) > 1:
    print(s.find(c), s.rfind(c))
else: print("-1")

# F61
s, c = input(), input()
t = s.count(c)
if t > 1: s = s[:s.find(c)] + s[s.rfind(c) + 1:]
print(s)

# F62
s = input()
w = s.replace("1", "one")
print(w)

# F63
s, c = input(), input()
w = s.replace(c, " ")
print(w)

# F64
s, r = input(), " "
for i in range(len(s)):
    if i % 3 != 0:
        r += s[i]
print(r)

# F65
# a)
t, old, new = input(), input(), input()
k = len(old)
p = t.find(old)
while p >= 0:
    t = t[:p] + new + t[p+k:]
    p = t.find(old)
print(t)
# b)
import sys
fi, fo = open("input.txt"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
t, old, new = input(), input(), input()
k = len(old)
p = t.find(old)
while p >= 0:
    t = t[:p] + new + t[p+k:]
    p = t.find(old)
print(t)
fo.close()
fi.close()

# F66
from math import factorial
n = int(input())
s = str(factorial(n))
print(s.count("0"))

# F67
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
r, sp = " ", " "
for w in input().split():
    r += sp + w[0].upper() + w[1:len(w)].lower()
    sp = " "
print(r)
fo.close()

# F68
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
from math import sqrt
s = input()
x, y = s.count("E") - s.count("W"), s.count("N") - s.count("S")
print(round(sqrt(x*x + y*y), 2))
fo.close()