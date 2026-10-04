# F86
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
n = int(input())
a = [int(x) for x in input().split()]
k, s = 0, 0
for x in a:
    if x > 0 and x % 3 == 0:
        k += 1
        s += x
print(k, s/3 - k, sep = "\n")
fo.close()

# F87
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
k, n = int(input()), int(input())
d = n % k
if d > k - d: d = k - d
print(d)
fo.close()

# F88
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
n = int(input())
t = 0
for i in input().split(): t += int(i)
print(n*(n + 1) // 2 - t)
fo.close()

# F89
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
n = int(input())
t = 0
for i in input().split(): t += int(i)
print(n*(n + 1) // 2 - t)
A = [int(i) for i in input().split()]
sorted(A)
print(A[len(A) // 2])
fo.close()

# F90
# Thuật toán 1:
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
g = sorted([float(i) for i in input().split()], reverse = True)
k = g.count(g[0])
res2 = g[k]
res1 = g.count(res2)
print(res1, res2)
fo.close()
# Thuật toán 2:
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
g = [float(i) for i in input().split()]
mx = max(g)
for i in range(len(g)):
    if g[i] == mx: g[i] = 0
mx = max(g)
print(g.count(mx), mx)
fo.close()