def reverse_array(arr):
    n=len(arr)
    first=0
    last=n-1
    while first<=last:
        arr[first],arr[last]=arr[last],arr[first]
        first+=1
        last-=1
    return arr

arr=[1,4,3,2,6]
print(reverse_array(arr))