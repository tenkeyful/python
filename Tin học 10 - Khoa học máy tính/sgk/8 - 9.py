# SGK/81
for _ in range(1, 5):
    print("Hello World!")

# SGK/81
n = int(input("n = "))
sum = 0
for i in range(1, n):
    if i % 3 == 0: sum += 1
print("Tổng của các số tự nhiên nhỏ hơn", n, "và chia hết cho 3 là:", sum)

# SGK/82
password = input("Nhập mật khẩu: ")
while (password != "HN123"):
    password = input("Nhập mật khẩu: ")
print("Bạn đã nhập mật khẩu.")

# SGK/82
sodem = 1
while (sodem <= 6):
    print(sodem)
    sodem += 1

# SGK/83
for counter in range(1, 11):
    print(counter, counter + counter)

# SGK/83
T = float(input("Nhập số tiền: "))
for i in range(10):
    T = T * (1 + 5/100)
    print(T)

# SGK/83
n = int(input("n = "))
i = 2
so_uoc = 0
while i <= n / 2:
    if (n % i) == 0: so_uoc += 1
    i += 1
print(n, "có số ước thực sự là:", so_uoc)

# SGK/84
import math
n = int(input("n = "))
i = 2
so_uoc = 0
while i <= math.sqrt(n):
    if n % i == 0:
        so_uoc += 1
        if i != (n // i):
            so_uoc += 1
    i += 1
print(n, "có số ước thực sự là:", so_uoc)

# SGK/85
n = int(input("Nhập số con: "))
m = int(input("Nhập số chân: "))
for i in range(n):
    if 4 * i + 2 * (36 - i) == m: # số chó * 4 + số gà * 2 = tổng số chân
        print("Số gà là:", 36 - i)
        print("Số chó là:", i)

# SGK/85
bang = 6
for i in range(1, 11):
    print(bang, "x", i, "= ?")
    tra_loi = input()
    if tra_loi == "dừng": break
    if tra_loi == "bỏ qua":
        print("Không nhớ, bỏ qua.")
        continue
    dap_an = i * bang
    if int(tra_loi) == dap_an:
        print("Đúng!")
    else:
        print("Sai! Đáp án:", dap_an)
print("Kết thúc.")

# SGK/85
p = 0
while True:
    print("Người tình nguyện:")
    tuổi = int(input("Tuổi: "))
    if tuổi == 0: break
    cao = float(input("Cao (m): "))
    nặng = float(input("Nặng (kg): "))

    if (18 <= tuổi <= 65 and not (18.5 <= nặng/cao**2 <= 22.9)): continue
    p += 1
print("Số người được xét:", p)