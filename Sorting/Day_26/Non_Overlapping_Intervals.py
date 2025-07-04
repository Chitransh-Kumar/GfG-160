def non_overlapping_intervals(arr):
    n=len(arr)
    arr.sort(key=lambda x:x[1])

    cnt=1
    non_overlap=arr[0][1]

    for i in range(1,n):
        if arr[i][0]>=non_overlap:
            cnt+=1
            non_overlap=arr[i][1]
    
    return n-cnt

arr=[[1,3],[2,3],[3,4],[1,2]]
print(non_overlapping_intervals(arr))