import sys
def max_product_subarray(arr):
    n=len(arr)
    prefix=1
    suffix=1
    max_product=-sys.maxsize-1

    for i in range(n):
        if prefix==0:
            prefix=1
        if suffix==0:
            suffix=1
        prefix=prefix*arr[i]
        suffix=suffix*arr[n-1-i]
        max_product=max(max_product,max(prefix,suffix))
    return max_product

arr=[-2,6,-3,-10,0,2]
print(max_product_subarray(arr))