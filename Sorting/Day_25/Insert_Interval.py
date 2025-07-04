def insert_interval(arr, newinterval):
    n=len(arr)
    i=0
    ans=[]

    while i<n and newinterval[0]>arr[i][1]:
        ans.append(arr[i])
        i+=1

    while i<n and newinterval[1]>arr[i][0]:
        newinterval[0]= min(arr[i][0],newinterval[0])
        newinterval[1]= max(arr[i][1],newinterval[1])
        i+=1
    ans.append(newinterval)

    while i<n:
        ans.append(arr[i])
        i+=1
    
    return ans

arr=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newinterval=[4,9]
print(insert_interval(arr,newinterval))