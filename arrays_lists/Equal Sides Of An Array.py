def find_even_index(arr):
    if not arr:
        return 0
    left = 0
    right = sum(arr)

    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])
        if left == right:
            return i
    return -1
