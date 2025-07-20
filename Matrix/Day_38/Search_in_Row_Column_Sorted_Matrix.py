def search_in_row_column_sorted_matrix(matrix, target):
    rows=len(matrix)
    cols=len(matrix[0])
    
    row=0
    col=cols-1
    while row<rows and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        else:
            col-=1
    
    return False

matrix=[[3,30,38],[20,52,54],[35,60,69]]
target=54

print(search_in_row_column_sorted_matrix(matrix,target))