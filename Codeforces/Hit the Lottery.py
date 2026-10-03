# def & while
def Withdraw_Cash(Balance):
    Bill_1, Bill_5, Bill_10, Bill_20, Bill_100 = 0, 0, 0, 0, 0
    while Balance >= 100:
        Bill_100 += 1
        Balance -= 100
    while Balance >= 20:
        Bill_20 += 1
        Balance -= 20
    while Balance >= 10:
        Bill_10 += 1
        Balance -= 10
    while Balance >= 5:
        Bill_5 += 1
        Balance -= 5
    while Balance >= 1:
        Bill_1 += 1
        Balance -= 1
    return [Bill_100, Bill_20, Bill_10, Bill_5, Bill_1]

print(Withdraw_Cash(3750))