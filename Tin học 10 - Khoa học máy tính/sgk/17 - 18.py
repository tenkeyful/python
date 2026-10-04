# SGK/117
n = int(input("Liều vacxin cần dự trữ: "))
m = int(input("Liều vacxin đang có trong kho: "))
pa = int(input("Liều cơ sở A sản xuất được mỗi ngày: "))
pb = int(input("Liều cơ sở B sản xuất được mỗi ngày: "))
t = 0

while m + (pa + pb) * t < n:
    t += 1
print("Số ngày cần thiết là", t)

# SGK/118
W = int(input("Dung lượng tối đa đĩa có thể lưu trữ: "))
print("Dung lượng của từng bức tranh:")

ds = [int(i) for i in input().split()]
ds.sort()
t = 0
s = 0

for i in range(0, len(ds)):
    s += ds[i]
    if s <= W:
        t += 1
    else: break
print("Số lượng tối đa các bức ảnh có thể ghi vào đĩa là:", t)