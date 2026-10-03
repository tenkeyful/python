def Anton(k2, k3, k5, k6):
    # Max_256 = min(5, 3, 4) = 3
    Max_256 = min(k2, k5, k6)
    # Max_32 = min(1, 5 - 3) = 1
    Max_32 = min(k3, k2 - Max_256)

    return (Max_256 * 256) + (Max_32 * 32)

k2, k3, k5, k6 = 5, 1, 3, 4
print(f"Maximum Sum: {Anton(k2, k3, k5, k6)}")