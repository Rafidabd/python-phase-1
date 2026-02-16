def insert_position(arr,target,low,high):
    if low>high:
        return low
    mid=(low+high)//2
    if arr[mid]>=target:
        return insert_position(arr,target,low,mid-1)
    else:
        return insert_position(arr,target,mid+1,high)
    
arr = [1,2,2,2,3,4]
pos = insert_position(arr, 5, 0, len(arr)-1)
print(pos)


