inv = {
    'Sword': 1,
    'Potion': 3
}

loot = {
    'Sword': 1,
    'Potion': 2,
    'Shield': 1
}

# Dictionary Comprehension 1
new_inv = {
    k: inv.get(k, 0) + loot.get(k, 0)
    for k in set(inv | loot) # Merge 2 dict via |
}
print(new_inv)

# Tìm tần số
a = [1, 2, 3, 5, 4, 1, 9, 8, 2, 7, 5, 6]
print(max(set(a), key = a.count)) #max(set, ...)

# Dictionary Comprehension 2
names = [
    "John",
    "Mike",
    "Roy",
    "James"
]

length = {name: len(name) for name in names}
print(length)