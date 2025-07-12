def student_num(arr, pages):
    n=len(arr)
    
    students=1
    student_pages=0
    for i in range(n):
        if student_pages+arr[i]<=pages:
            student_pages+=arr[i]
        else:
            students+=1
            student_pages=arr[i]

    return students

def allocate_minimum_pages(arr, k):
    n=len(arr)

    if k>n:
        return -1
    
    low=max(arr)
    high=sum(arr)

    ans=-1
    while low<=high:
        mid=(low+high)//2
        student_count=student_num(arr,mid)
        if student_count<=k:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans


arr=[15,10,19,10,5,18,7]
k=5

print(allocate_minimum_pages(arr,k))