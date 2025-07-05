def merge_without_extra_space(arr1, arr2):
    n1=len(arr1)
    n2=len(arr2)

    left=n1-1
    right=0
    while left>=0 and right<n2:
        if arr1[left]>arr2[right]:
            arr1[left],arr2[right]=arr2[right],arr1[left]
            left-=1
            right+=1
        else:
            break
    
    arr1.sort()
    arr2.sort()

    return arr1,arr2

arr1=[1,5,9,10,15,20]
arr2=[2,3,8,13]
print(merge_without_extra_space(arr1,arr2))