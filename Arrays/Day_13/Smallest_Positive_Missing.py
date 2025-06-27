def smallest_positive_missing(arr):
    n=len(arr)

    for i in range(n):
        while 1<=arr[i]<=n and arr[i]!=arr[arr[i]-1]:
            correct_index=arr[i]-1
            arr[i],arr[correct_index]=arr[correct_index],arr[i]
        
    ans=n+1
    for i in range(n):
        if arr[i]!=i+1:
            ans=i+1
            break
    
    return ans
    

arr=[5,3,2,5,1]
print(smallest_positive_missing(arr))