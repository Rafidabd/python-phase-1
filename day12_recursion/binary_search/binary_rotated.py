"""
task:Array is sorted but rotated:

[4,5,6,7,0,1,2]


Find target efficiently.


Approach:
If left side is sorted:
    If target in left range -go left
    Else - go right
Else:
    Right side is sorted
    If target in right range - go right
    Else -go left



"""

def func_rotated(arr,target,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    if arr[mid]>=arr[low]:  #if left side is sorted
        if target<=arr[mid] and target>=arr[low]: #does the target stays in the left portion??
            return func_rotated(arr,target,low,mid-1)
        else :
            return func_rotated(arr,target,mid+1,high) #if not,then obviously in the right portion
    else:  #If right side is sorted
        if target>=arr[mid] and target<=arr[high]:
            return func_rotated(arr,target,mid+1,high) #does the target stays in the right portion
        else :
            return func_rotated(arr,target,low,mid-1) #if not,then obviously at the left portion
        

#Time complexity: O(log n)



       
        

        

    
    