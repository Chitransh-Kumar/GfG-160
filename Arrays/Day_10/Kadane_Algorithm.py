import sys
def kadane_algorithm(arr):
    n=len(arr)
    max_sum=-sys.maxsize-1
    sum=0
    
    for i in range(n):
        sum=sum+arr[i]
        if sum>max_sum:
            max_sum=sum
        if sum<0:
            sum=0
    
    return max_sum

arr=[2,3,-8,7,-1,2,3]
print(kadane_algorithm(arr))