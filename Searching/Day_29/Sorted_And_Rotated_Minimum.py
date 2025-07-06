import sys

def sorted_and_rotated_minimum(arr):
    n=len(arr)

    low=0
    high=n-1
    minimum=sys.maxsize
    
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            minimum=min(arr[low],minimum)
            low=mid+1
        else:
            minimum=min(arr[mid],minimum)
            high=mid-1

    return minimum

arr=[5,6,1,2,3,4]
print(sorted_and_rotated_minimum(arr))