# F83
p, q = map(int, input().split())
a = [int(i) for i in input().split()]
p -= 1
print(min(a[p:q]), max(a[p:q]))

# F84
from math import sqrt
def distance(x, y, u, v):
    return sqrt((x - u)**2 + (y - v)**2)
n = int(input())
res = 0
x, y = map(int, input().split())
x0, y0 = x, y
for i in range(1, n):
    u, v = map(int, input().split())
    res = max(res, distance(x, y, u, v))
    x, y = u, v
res = max(res, distance(x, y, x0, y0))
print(round(res, 2))

# F85
Trace = input()
dr = "ENWS"
p, q = Trace.count("L"), Trace.count("R")
k = (p + 3*q) % 4
print(dr[k])