def search_in_sorted_matrix(matrix,target):
    rows=len(matrix)
    cols=len(matrix[0])

    start=0
    end=rows*cols-1
    while start<=end:
        mid=(start+end)//2

        row=mid//cols
        col=mid%cols
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            end=mid-1
        else:
            start=mid+1
    
    return False

matrix=[[1,5,9],[14,20,21],[30,34,43]]
target=29

print(search_in_sorted_matrix(matrix,target))