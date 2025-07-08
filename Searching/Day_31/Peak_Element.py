def peak_element(arr):
    n=len(arr)

    if n==1:
        return 0
    
    if arr[0]>arr[1]:
        return 0
    
    if arr[n-1]>arr[n-2]:
        return n-1
    
    start=1
    end=n-2
    while start<=end:
        mid=(start+end)//2

        if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            start=mid+1
        else:
            end=mid-1

arr=[1,2,4,5,7,8,3]
print(peak_element(arr))