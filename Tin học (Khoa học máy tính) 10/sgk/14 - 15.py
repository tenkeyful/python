# SGK/100
s = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
i = int(input("Nhập một chữ số: "))
print(s[i])

# SGK/104
friends = ['Mai', 'Minh', 'Nga', 'Anh', 'Giang', 'Lan']
friends.append('Hoa')
friends.pop(2)
friends.insert(0, 'Phan')
friends.sort()
tuple(friends) #Immutable
print(friends)

name = input("Tên: ")
if name in friends:
    print("Chấp nhận quyền truy cập.")
else:
    print("Quyền truy cập bị từ chối.")

# SGK/105
car_licenses = [int(i) for i in input("Nhập mã xe: ").split()]
car_licenses.sort()
print(car_licenses)

t = 1
for i in range(1, len(car_licenses)):
    if car_licenses[i] != car_licenses[i - 1]:
        t += 1
print(t)

# SGK/107
print ("Nhập dãy số nguyên:")
a = [int(i) for i in input().split()]

for i in range(len(a)):
    if a[i] > 0: a[i] = 1
    elif a[i] < 0: a[i] = -1
for i in a: print(i, end=' ')

# SGK/108
print("Nhập một dãy số nguyên")
a, count = [int(i) for i in input().split()], 0

for i in range (1, len(a)-1):
    if a[i-1] < a[i] > a[i + 1]: count += 1
print(count)

# SGK/109
print("Nhập vào một dãy số size giày")
shoes, sum = [int(s) for s in input().split()], 0

for i in range(len(shoes)):
    sum += shoes[i]

if sum > 0: print("Chiếc giày bên trái, kích cỡ", sum)
else: print("Chiếc giày bên phải, kích cỡ", sum)