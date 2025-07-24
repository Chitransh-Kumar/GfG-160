def find_all_triplets_with_zero_sum(arr):
    n=len(arr)

    hash_set=set()

    for i in range(n):
        hash_map={}
        for j in range(i+1,n):
            search_num=-(arr[i]+arr[j])
            if search_num in hash_map:
                temp=[hash_map[search_num],i,j]
                temp.sort()
                hash_set.add(tuple(temp))
            hash_map[arr[j]]=j

    return list(hash_set)

arr=[1,-2,1,0,5]
arr=[0,-1,2,-3,1]

print(find_all_triplets_with_zero_sum(arr))