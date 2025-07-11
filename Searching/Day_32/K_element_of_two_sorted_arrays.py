def kth_element_of_two_sorted_arrays(arr1, arr2, k):
    n1=len(arr1)
    n2=len(arr2)

    first=0
    second=0
    cnt=1

    while first<n1 and second<n2:
        if arr1[first]<arr2[second]:
            if cnt==k:
                return arr1[first]
            cnt+=1
            first+=1
        else:
            if cnt==k:
                return arr2[second]
            cnt+=1
            second+=1

    while first<n1:
        if cnt==k:
            return arr1[first]
        cnt+=1
        first+=1
    
    while second<n2:
        if cnt==k:
            return arr2[second]
        cnt+=1
        second+=1
    
    return -1

arr1=[100,112,256,349,770]
arr2=[72,86,113,119,265,445,892]
k=7

print(kth_element_of_two_sorted_arrays(arr1, arr2, k))
