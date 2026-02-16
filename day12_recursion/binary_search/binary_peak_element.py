"""
If arr[mid] < arr[mid+1]:
    peak ∈ (mid+1, high]
Else:
    peak ∈ [low, mid]


"""


def peak_element(arr,low,high):
    if low==high:
        return arr[low]
    mid=(low+high)//2
   
    if arr[mid]>arr[mid+1]:
        return peak_element(arr,low,mid)
    else:
        return peak_element(arr,mid+1,high)
    
arr=[1,2,2,3,4,5,1,2,3]
print(peak_element(arr,0,len(arr)-1))