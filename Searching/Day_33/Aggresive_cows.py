def can_be_placed(arr, dist, cows):
    n=len(arr)
    count_cows=1
    last_cow=arr[0]

    for i in range(1,n):
        if arr[i]-last_cow>=dist:
            count_cows+=1
            last_cow=arr[i]
            if count_cows>=cows:
                return True        
    
    return False


def aggressive_cows(arr, cows):
    n=len(arr)

    arr.sort()
    low=1
    high=arr[n-1]-arr[0]

    ans=-1
    while low<=high:
        mid=(low+high)//2
        if can_be_placed(arr, mid, cows)==True:
            ans=mid
            low=mid+1
        else:
            high=mid-1

    return ans

stalls=[2,12,11,3,26,7]
k=5
print(aggressive_cows(stalls,k))