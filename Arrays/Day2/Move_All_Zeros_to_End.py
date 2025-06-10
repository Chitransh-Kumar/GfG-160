def move_zeros_to_end(arr):
    n=len(arr)
    start=0
    end=0
    while start<n:
        if arr[start]!=0 and arr[end]!=0:
            end+=1
        elif arr[start]!=0 and arr[end]==0:
            arr[start],arr[end]=arr[end],arr[start]
            end+=1
        start+=1
    return arr

arr=[1,2,0,4,3,0,5,0]    
print(move_zeros_to_end(arr))