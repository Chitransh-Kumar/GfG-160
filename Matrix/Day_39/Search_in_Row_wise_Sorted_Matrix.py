def search_in_row_wise_sorted_matrix(matrix,target):
    row=len(matrix)
    col=len(matrix[0])

    for i in range(row):
        if matrix[i][0]<=target and target<=matrix[i][col-1]:
            start=0
            end=col-1
            while start<=end:
                mid=(start+end)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    end=mid-1
                else:
                    start=mid+1

    return False

matrix=[[3,4,9],[2,5,6],[9,25,27]]
target=8

print(search_in_row_wise_sorted_matrix(matrix,target))