def second_largest(arr):
    maximum=-1
    n=len(arr)

    for i in range(n):
        if arr[i]>maximum:
            maximum=arr[i]
    
    second_max=-1

    for i in range(n):
        if arr[i]>second_max and arr[i]!=maximum:
            second_max=arr[i]
    
    return second_max

arr=[1,2,0,4,3,0,5,0]

print(second_largest(arr))