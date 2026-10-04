Hồi cấp 3, mình được giới thiệu đến ngôn ngữ lập trình Python. Mặc dù trường lúc đó không yêu cầu bắt buộc học ngoài chương trình, mình học thêm vì niềm yêu đối với lập trình.

Đây là những bài tập mình thấy thú vị mà được giới thiệu trong sách của bộ sách Cánh diều:

Bài tập Tin học 10

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
- Đảo dấu vàng
```
# Cách 1
import math

s = input()
x = s.count("E") - s.count("W")
y = s.count("N") - s.count("S")

print(math.sqrt(x**2 + y**2))

# Cách 2
import math

duong_di = input("")

x = 0
y = 0

for huong in duong_di:
    if huong == "E":
        x += 1
    elif huong == "W":
        x -= 1
    elif huong == "N":
        y += 1
    elif huong == "S":
        y -= 1

print(math.sqrt(x**2 + y**2))
```


Tin học 11 - Khoa học máy tính


Bài tập Tin học 11

- Dãy số Catalan (F<sup>CS</sup>5 trang 43)
```

```

- Tam giác Pascal (F<sup>CS</sup>7 trang 44)
```

```

- Bài toán Josephus (F<sup>CS</sup>45 trang 65)
```

```

Chuyên đề học tập Tin học 11 - Khoa học máy tính
