def number_of_occurence(arr,target):
    n=len(arr)

    # First Occurence
    
    start=0
    end=n-1
    first_occurence=-1
    
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            first_occurence=mid
            end=mid-1
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1

    if first_occurence==-1:
        return 0
    
    # Last Occurence

    start=0
    end=n-1
    last_occurence=-1

    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            last_occurence=mid
            start=mid+1
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1

    return last_occurence-first_occurence+1

arr=[1,1,2,2,2,2,3]
target=2

print(number_of_occurence(arr,target))