#given array a of size n, rotate it d time to the left

def rotLeft(a, d):
    # Write your code here
    for counter in range(d):
        a.append(a.pop(0))
    return a


print(rotLeft([33, 47, 70, 37, 8, 53, 13,
      93, 71, 72, 51, 100, 60, 87, 97], 13))
print(rotLeft([1, 2, 3, 4, 5], 4))
