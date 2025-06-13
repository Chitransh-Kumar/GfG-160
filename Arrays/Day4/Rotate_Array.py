def rotate_array(arr,d):
    n=len(arr)
    d=d%n
    temp=[0]*d

    for i in range(d):
        temp[i]=arr[i]

    for i in range(d,n):
        arr[i-d]=arr[i]

    for i in range(d):
        arr[n-d+i]=temp[i]
    
    return arr

arr=[7,3,9,1]
d=9

print(rotate_array(arr,d))