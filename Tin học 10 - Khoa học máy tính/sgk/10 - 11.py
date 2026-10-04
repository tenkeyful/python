# SGK/91
def dientichtg(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    return s**0.5

a, b, c = 3, 4, 5
u, v, w = 4,6, 7
p, q, r = 3.5, 4.5, 6

s1 = dientichtg(a, b, c)
s2 = dientichtg(u, v, w)
s3 = dientichtg(p, q, r)

print("Diện tích tam giác lớn nhất là: ", max(s1, s2, s3))

# SGK/93
import time
tb = time.time()
n = 0
s = 0
x = int(input())

while x > 0:
    n += 1
    s += x
    x = int(input())
if n > 0: print("Trung bình cộng: ", s/n)
print("\nTime: %.4f sec"%(time.time()-tb))

# SGK/93
def Drawbox(a):
    for i in range(a):
        for j in range(10):
            print("#", end = "")
        print()

a = int(input("a = "))
Drawbox(a)