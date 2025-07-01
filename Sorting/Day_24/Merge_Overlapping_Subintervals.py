def merge_overlapping_subintervals(arr):
    n=len(arr)
    arr.sort()
    ans=[arr[0]]
    
    for i in range(1,n):
        if ans[-1][1]>=arr[i][0]:
            ans[-1][1]=max(ans[-1][1],arr[i][1])
        else:
            ans.append(arr[i])
    
    return ans

arr=[[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
print(merge_overlapping_subintervals(arr))