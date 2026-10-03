# F73
import sys
fi, fo = open("input.txt"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
for i in input().split():
    if int(i) % 2 == 0: print(i, end = "")
fo.close()

# F74
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
for i in input().split():
    if int(i) > 0: print(i, end = "")
fo.close()

# F75
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if a[i] > a[i - 1]: print(a[i], end = " ")
fo.close()

# F76
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
a = [int(i) for i in input().split()]
v = max(a)
p = a.index(v) + 1
print(v, p)
fo.close()

# F77
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
a = [int(i) for i in input().split()]
k = 0
for i in range(len(a)):
    if a[i] != 0:
        a[k] = a[i]
        k += 1
for i in range(k, len(a)): a[i] = 0
for i in a: print(i, end = " ")
fo.close()

# F78
import sys
fi, fo = open("input.txt", encoding = "utf-8"), open("output.txt", "w", encoding = "utf-8")
sys.stdin, sys.stdout = fi, fo
a = [int(i) for i in input().split()]
ans = "Yes"
for i in range(1, len(a)):
    if a[i - 1] > a[i]:
        ans = "No"
        break
print(ans)
fo.close()

# F80
a = [int(i) for i in input().split()]
b = [a[0]]
print(b[0], end = " ")
for i in range(1, len(a)):
    b.append(b[i - 1] + a[i])
    print(b[i], end = " ")