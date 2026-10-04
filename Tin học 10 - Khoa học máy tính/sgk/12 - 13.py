# SGK/95
name = input("Bạn tên là gì? ")
print(len(name))

x = "ABC"
y = "1234"
z = "cba"
r = x + y + z
print(r)

y = "abc1234abc1234abc1234"
print(y.count("a"))
x = "c12"
print(y.count(x, 3))
y = "aaa"
x = "aa"
print(y.count(x))

y = "0123456"
print(y[2:5])
print(y[2])

y = "Cái xắc xinh xinh"
x = "xinh"
z = "bé"
print(y.find(x))
print(y.find(z))

y = "Trúc xinh trúc mọc sân đình"
x1 = "sân đình"
x2 = "bờ ao"
print(y.replace(x1, x2))

a = " Trúc xinh trúc mọc bờ ao"
b = " Em xinh em đúng nơi nào cũng xinh"
print(a, b)
print(
    a.replace("bờ ao", "sân đình"),
    b.replace("nơi nào", "một mình")
)

# SGK/97
xau1 = "Hà Nội là Thủ đô của nước Việt Nam."
xau2 = "Nam Khánh sinh ra ở Hà Nội"
xau = xau1 + xau2
print(xau)
print(xau.count("N", 6))
print(xau.find("Khánh"))
print(xau[25:34])
print(xau.replace("Khánh", "An"))

# SGK/97
date_of_birth = input("Nhập ngày tháng năm sinh: ")
dd = date_of_birth[0:2]
mm = date_of_birth[3:5]
yyyy = date_of_birth[6:10]
s = "Ngày " + dd + " tháng " + mm + " năm " + yyyy
print(s)

# SGK/97
s1 = input("Nhập xâu 1: ")
s2 = input("Nhập xâu 2: ")
s3 = s1 + " "+ s2
t = 1

for ch in s3:
    if ch == " ":
        t = t + 1
print("Số từ:", t)

# SGK/100
s = input('Dòng lệnh: ')
e = s.count('E')
w = s.count('W')
n = s.count('N')
s = s.count('S')

x = e - w
y = n - s
print('Toạ độ hiện tại của robot: (%s, %s)' %(x, y))