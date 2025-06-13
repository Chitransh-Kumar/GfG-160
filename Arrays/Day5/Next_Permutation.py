def next_permutation(arr):
    n=len(arr)
    index_1=-1
    
    # When we see from back of array the array increses and then decreases. 
    # We need to find point where it has transition.
    # Find index_1 which is transition point.
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            index_1=i
            break
    
    # If there is no transition point, means array is only increasing. 
    # Thus we then return the reversed number which is the smallest number.
    if index_1==-1:
        return arr[::-1]

    # We see from back of array and find the first number which is greater than arr[index_1]
    # We call it arr[index_2]
    index_2=-1
    for i in range(n-1,index_1,-1):
        if arr[i]>arr[index_1]:
            index_2=i
            break
    
    # We swap arr[index_1] and arr[index_2]
    arr[index_1],arr[index_2]=arr[index_2],arr[index_1]

    # We reverse numbers from index_1+1 to end of the array
    i=index_1+1
    j=n-1
    while i<=j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    
    return arr

arr=[2,4,1,7,5,0]
print(next_permutation(arr))