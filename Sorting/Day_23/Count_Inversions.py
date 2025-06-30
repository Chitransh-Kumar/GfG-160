def merge(arr, low, mid, high):
    cnt=0
    temp=[]
    left=low
    right=mid+1
    
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            cnt+=(mid-left+1)
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1
    
    while right<=high:
        temp.append(arr[right])
        right+=1

    for i in range(len(temp)):
        arr[low+i]=temp[i]
    
    return cnt

def merge_sort(arr, low, high):
    cnt=0
    if low>=high:
        return 0

    mid= (low+high)//2

    cnt+=merge_sort(arr, low, mid)

    cnt+=merge_sort(arr, mid+1, high)

    cnt+=merge(arr, low, mid, high)

    return cnt

def count_inversions(arr):
    return merge_sort(arr, 0, len(arr)-1)
    
arr=[1,9,3,5,7,8,2,4]
print(count_inversions(arr))