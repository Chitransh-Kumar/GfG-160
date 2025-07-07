def search_in_rotated_sorted_array(arr, target):
    n=len(arr)
    
    index=-1
    start=0
    end=n-1
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==target:
            index=mid
            break
        
        if arr[start]<=arr[mid]: # Left-half sorted
            if arr[start]<=target and target<=arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else: # Right-half sorted
            if arr[mid]<=target and target<=arr[end]:
                start=mid+1
            else:
                end=mid-1
    
    return index

arr=[3,5,1,2]
target=6

print(search_in_rotated_sorted_array(arr, target))