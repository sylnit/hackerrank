def hourglassSum(arr):
    # Write your code here
    if isinstance(arr, list):
        hourglasses = []
        arrLen = len(arr)
        for row in range(4):
            for col in range(4):
                hg_sum = 0
                hg_sum += arr[row][col]
                hg_sum += arr[row][col+1]
                hg_sum += arr[row][col+2]
                hg_sum += arr[row+1][col+1]
                hg_sum += arr[row+2][col]
                hg_sum += arr[row+2][col+1]
                hg_sum += arr[row+2][col+2]
                hourglasses.append(hg_sum)
        return max(hourglasses)


hourglassSum([
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
)
