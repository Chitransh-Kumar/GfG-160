def sort_0_1_2_brute(arr):
    n=len(arr)

    cnt_0=0
    cnt_1=0
    cnt_2=0

    for i in range(n):
        if arr[i]==0:
            cnt_0+=1
        elif arr[i]==1:
            cnt_1+=1
        else:
            cnt_2+=1

    for i in range(0,cnt_0):
        if arr[i]!=0:
            arr[i]=0
    
    for i in range(cnt_0,cnt_0+cnt_1):
        if arr[i]!=1:
            arr[i]=1

    for i in range(cnt_0+cnt_1,n):
        if arr[i]!=2:
            arr[i]=2
    
    return arr

def sort_0_1_2(arr):
    n=len(arr)

    low=0
    mid=0
    high=n-1

    while mid<=high:
        if arr[mid]==0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    
    return arr

arr=[0,1,1,0,1,2,1,2,0,0,0,1]
print(sort_0_1_2(arr))