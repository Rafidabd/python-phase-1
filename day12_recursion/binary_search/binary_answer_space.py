#Recursion method:

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
    
print(first_occurance([1,2,3,4,5,6,6,7,8],6,0,8))






#Simplier Method:
def lower_bound(arr,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]>=target:
        return lower_bound(arr,target,low,mid-1)
    else:
        return lower_bound(arr,target,mid+1,high)
    
arr = [1,2,2,2,3,4]
pos = lower_bound(arr, 2, 0, len(arr)-1)

if pos < len(arr) and arr[pos] == 2:
    print("First occurrence at:", pos)
else:
    print("Not found")

    



    
    

