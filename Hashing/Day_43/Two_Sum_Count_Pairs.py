def two_sum_count_pairs(arr, target):
    n=len(arr)

    frequency={}

    cnt=0
    for i in range(n):
        search_num=target-arr[i]

        if search_num in frequency:
            cnt+=frequency[search_num]
        
        if arr[i] not in frequency:
            frequency[arr[i]]=1
        else:
            frequency[arr[i]]+=1
    
    return cnt

arr=[1,1,1,1]
target=2

print(two_sum_count_pairs(arr,target))