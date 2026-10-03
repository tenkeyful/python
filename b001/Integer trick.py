# Integer Trick
a = 1_000_000
b = 2_000
print(a / b)

# Clever One Liner
name = input("Name: ") or "N/A"
print(name)

# Merge_Int_Arrays
c = [1, 2, 3, 5, 3, 8, 10, 2]
d = [6, 7, 4, 10, 9, 6, 2 , 3]
print(sorted(set(c + d))) #remove dup elements and then sort out

# Sort_Str_Array
e = ['a', 'b', 'c', 'a', 'a', 'b', 'd', 'f']
    # Method 1:
e1 = []
for element in e:
    if element not in e1:
        e1.append(element) #Checks if element isnt in e1 and if so is added into it.
    # Method 2:
e2 = list(dict.fromkeys(e).keys()) #Create a dictionary with the keys from the provided list, returns the keys and turn into a list
print(e1, e2)

# Correct input value
balance = 500

while True:
    try:
        num = float(input("Deposit: "))
        break
    except ValueError:
        print("Must be a valid quantity.")

balance += num
print(f"Balance: {balance}")