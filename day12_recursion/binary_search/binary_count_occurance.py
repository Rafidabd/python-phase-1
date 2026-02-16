def first_occurance(arr,target,low,high):
    if low>high:
        return -1
   
    mid=(low+high)//2
    if arr[mid]==target :
        
        left= first_occurance(arr,target,low,mid-1)
        return mid if left==-1 else left
    elif arr[mid]>target:
        
        return first_occurance(arr,target,low,mid-1)
    else:
        return first_occurance(arr,target,mid+1,high)
    
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
    

def count_occurance(arr,target,low,high):
    x=first_occurance(arr,target,low,high)
    y=last_occurance(arr,target,low,high)
    z=(y-x)+1
    if x==-1:
        return 0
    else:
        return z
    
arr=[1,2,2,2,2,3,3,5,6,7,8,8,8]

print(count_occurance(arr,10,0,len(arr)-1))




