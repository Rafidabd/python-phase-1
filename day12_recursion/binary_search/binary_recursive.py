def binary_search(arr, target, low, high):
    if low > high:
        return -1   # base case

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)  # right side
    else:
        return binary_search(arr, target, low, mid - 1)   # left side


print(binary_search([1, 2, 3, 4, 5], 4, 0, 4))

    