def minimumSwaps(arr):
    swap_count = 0
    sorted_arr = sorted(arr)
    pos = 0
    while sorted_arr != arr:
        if pos == len(arr)-1:
            pos = 0
            continue

        if arr[pos] == pos+1:
            pos += 1
            continue
        else:
            next_pos = arr[pos]-1
            if arr[pos] > arr[next_pos]:
                swap_count += 1
                temp = arr[pos]
                arr[pos] = arr[next_pos]
                arr[next_pos] = temp
            pos += 1

    return swap_count


print(minimumSwaps([1, 3, 5, 2, 4, 6, 7]))
