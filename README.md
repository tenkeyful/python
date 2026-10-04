Hồi cấp 3, mình được giới thiệu với ngôn ngữ lập trình Python. Mặc dù trường lúc đó không bắt buộc học thêm ngoài chương trình, mình vẫn học vì niềm yêu thích đối với lập trình.

Đây là những thuật toán mà mình thấy hay được giới thiệu trong sách thuộc bộ sách Cánh diều:

##### [Tin học 10 - Khoa học máy tính](Tin%20học%2010%20-%20Khoa%20học%20máy%20tính)

##### Bài tập Tin học 10
- Giả thuyết Collatz (F54 trang 37)
```
n = int(input())

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1

print(n)
```
- Thuật toán Euclid (F43 trang 100)
```
# Cách 1
a = int(input("a = "))
b = int(input("b = "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)

# Cách 2
a = int(input("a = "))
b = int(input("b = "))

while b != 0:
    so_du = a % b
    a = b
    b = so_du

print("GCD =", a)
```

##### Tin học 11 - Khoa học máy tính
- Thuật toán sàng Eratosthenes (Bài 4 trang 105)
```
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2

    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False
    return prime
```
- Phép kiểm tra Miller-Rabin, Phép kiểm tra Solovay-Strassen (Bài 4 trang 106)

##### Bài tập Tin học 11
- Dãy số Catalan (F<sup>CS</sup>5 trang 43)
```
# Cách 1
n = int(input())

C = [1]
for i in range(1, n + 1):
    C_i = 0
    for j in range(i):
        C_i += C[j] * C[i - 1 - j]
    C.append(C_i)

print(*C)

# Cách 2
import math

for i in range(10):
    print(math.comb(2 * i, i) // (i + 1))
```
- Tam giác Pascal (F<sup>CS</sup>7 trang 44)
```
n = int(input())
C = []

for i in range(n + 1):
    C_i = [1]
    for j in range(1, i):
        C_i.append(C[i - 1][j - 1] + C[i - 1][j])
    if i > 0:
        C_i.append(1)
    C.append(C_i)

print(*C[n])
```
- Bài toán Josephus (F<sup>CS</sup>45 trang 65)
```
# Cách 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n = int(input())

head = Node(1)
node = head

for i in range(2, n + 1):
    node.next = Node(i)
    node = node.next
node.next = head

node = head
while n > 1:
    print(node.next.data, end = " ")
    node.next = node.next.next
    node = node.next
    n -= 1
print(node.data)

# Cách 2
n = int(input())

people = list(range(1, n + 1))

index = 0

while len(people) > 1:
    index = (index + 1) % len(people)
    print(people.pop(index), end=" ")

print(people[0])

# Cách 3
n = int(input())
survivor = 0

for i in range(2, n + 1):
    survivor = (survivor + 2) % i

print(survivor + 1)
```

##### Chuyên đề học tập Tin học 11 - Khoa học máy tính
