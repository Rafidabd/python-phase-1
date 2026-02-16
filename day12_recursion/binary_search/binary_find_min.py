def find_min(arr,low,high):
    mid=(low+high)//2
    if arr[mid]<=arr[mid+1] and arr[mid]<=arr[mid-1]:
        return arr[mid]
    mid=(low+high)//2
    if arr[mid]>=arr[high]:
       return find_min(arr,mid+1,high)
    else:
        return find_min(arr,low,mid-1)
    


arr=[4,5,6,7,1,2,2,3]

print(find_min(arr,0,len(arr)-1)) 
    

    
    
    

