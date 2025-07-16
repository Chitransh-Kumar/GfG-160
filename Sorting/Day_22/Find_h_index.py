def find_h_index(arr):
    n=len(arr)

    paper_counts=[0]*(n+1)

    for i in range(n):
        if arr[i]<n:
            paper_counts[arr[i]]+=1
        else:
            paper_counts[n]+=1

    papers=0
    
    for i in range(n,-1,-1):
        papers=papers+paper_counts[i]

        if papers>=i:
            return i
        
    return 0

arr=[5,1,2,8,9,3]

print(find_h_index(arr))