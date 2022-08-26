def getPosition(array, val):
    for i in range(len(array)):
        if array[i] == val:
            return i
    return -1


def minimumBribes(q):
    # Write your code here
    data = list(range(1, len(q)+1))
    num_of_bribes = 0

    for i in range(len(q)):
        pos = getPosition(data, q[i])
        data.pop(pos)

        if pos > 2:
            print("Too chaotic")
            return
        num_of_bribes += pos
    print(num_of_bribes)


print(minimumBribes([2, 1, 5, 3, 4]))
