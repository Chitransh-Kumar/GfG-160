def kth_missing_positive_number_in_sorted_array(arr, k):
    n=len(arr)

    if k<arr[0]:
        return k

    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2

        missing=arr[mid]-(mid+1)
        if missing>=k:
            high=mid-1
        else:
            low=mid+1
        
    ans=k+high+1
    return ans

arr=[2,3,5,6]
k=2

print(kth_missing_positive_number_in_sorted_array(arr,k))