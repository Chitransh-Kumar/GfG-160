def two_sum(arr, target):
    n=len(arr)

    hash_map={}

    for i in range(n):
        search_num=target-arr[i]

        if search_num in hash_map:
            return True
        hash_map[arr[i]]=i

    return False

arr=[1,2,1,2,3]
target=0

print(two_sum(arr,target))