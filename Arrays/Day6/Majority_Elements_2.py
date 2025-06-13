import sys

def majority_elements_2(arr):
    n=len(arr)
    ans=[]
    
    count_1=0
    element_1=-sys.maxsize-1

    count_2=0
    element_2=-sys.maxsize-1

    for i in range(n):
        if count_1==0 and arr[i]!=element_2:
            element_1=arr[i]
            count_1+=1
        elif count_2==0 and arr[i]!=element_1:
            element_2=arr[i]
            count_2+=1
        elif arr[i]==element_1:
            count_1+=1
        elif arr[i]==element_2:
            count_2+=1
        else:
            count_1-=1
            count_2-=1

    # Cross check if the elements have occurence greater than n/3.
    count_1=0
    
    for i in range(n):
        if arr[i]==element_1:
            count_1+=1
    
    if count_1>n//3:
        ans.append(element_1)

    count_2=0
    
    for i in range(n):
        if arr[i]==element_2:
            count_2+=1
    
    if count_2>n//3:
        ans.append(element_2)
    
    return ans

arr=[-1,-1,-1]
print(majority_elements_2(arr))