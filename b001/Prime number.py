# Xác định số nguyên tố
def IS_NUM_PRIME(n): # Chia hết cho 1 và chính nó.
  for k in range(2, int(n**0.5) + 1):
    # (math.sqrt(n) = n**0.5)
    """
    VD: căn(16) = 16^0.5 = 4

    Công thức: k = (x^0.5) + 1
    k = 2 → 2,414...
    k = 3 → 2,732...
    k = 4 → 3
    Kết luận: 2 và 3 là số nguyên tố và 4 không phải là số nguyên tố.
    VD: 2 không chia hết cho bất kỳ tập con nào trong tập k. Cũng như 3. Nhưng 4 chia hết vì k có tập con 2 mà 4 % 2 == 0.
    k = 9 → 4; k = 16 → 5; k = 25 → 6
    """
    if n % k == 0:
      return False # ko phải là số nguyên tố
  return True # số nguyên tố

t = []
for j in range(2, 1001): # 1 ko phải là số nguyên tố nên bắt đầu từ 2. j chạy từ 2 đến 1000
  if IS_NUM_PRIME(j):
    t.append(j)
print(t)

# www. remover
links = [
    "youtube.com",
    "wikiwand.com",
    "ldoceonline.com",
    "bing.com",
    "minecraft.net"
]

for link in links:
    print(link.removeprefix("www."))