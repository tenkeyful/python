# O(n^2)
def Josephus_Permutation(array, k):
    permutation = []
    i = 0 # index
    while array:
        i = (i + k - 1) % len(array)
        item = array.pop(i)
        permutation.append(item)
    return permutation

soldiers = 41
soldier_list = [n + 1 for n in range(soldiers)]
k = 3

solution = Josephus_Permutation(soldier_list, k)
print(solution)

# O(n)
def Sort_List(array):
    t, z = [], 0
    for i in array: # O(n)
        if i != 0:
            t.append(i) # O(1)
        else:
            z += 1 # O(1)
    t.extend(z * [0]) # O(n) but doesn't compound since it's outside the for loop statement
    return t

from random import randint
n = 100
n_array = [randint(0, 9) for _ in range(n)]
print(Sort_List(n_array))