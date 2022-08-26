def largest(array):

    if len(array) == 0:
        return print("Too Small")

    max_sum = current_sum = array[0]

    for num in array[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(max_sum, current_sum)

    return max_sum


print(largest([7, 1, 2, -1, 3, 4, 10, -12, 3, 21, -19]))
