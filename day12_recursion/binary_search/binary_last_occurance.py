#recursive method:
def last_occurance(arr,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        right=last_occurance(arr,target,mid+1,high)
        return mid if right==-1 else right
    elif target<arr[mid]:
        return last_occurance(arr,target,low,mid-1)
    else:
        return last_occurance(arr,target,mid+1,high)
    
# arr=[1,2,2,2,3,4,5,5,5,6]
# print(last_occurance(arr,5,0,len(arr)-1))

#higher bound:
def higher_bound(arr,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]<=target:
        return higher_bound(arr,target,mid+1,high)
    else:
        return higher_bound(arr,target,low,mid-1)
    
arr = [1,2,2,2,3,4]
pos = higher_bound(arr, 2, 0, len(arr)-1)

if pos >len(arr) and arr[pos] == 2:
    print("last occurrence at:", pos)
else:
    print("Not found")







