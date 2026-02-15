def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


# test
arr = [1, 3, 5, 7, 9, 11]
print(binary_search_iterative(arr, 9)) 
