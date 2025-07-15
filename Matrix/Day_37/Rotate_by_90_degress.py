def rotate_by_90_degrees(matrix):
    n=len(matrix)

    # Transpose of the matrix
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    # Row swap for each column
    for j in range(n):
        top=0
        bottom=n-1
        while top<=bottom:
            matrix[top][j],matrix[bottom][j]=matrix[bottom][j],matrix[top][j]    
            top+=1
            bottom-=1

    return matrix
    
matrix=[[0,1,2],[3,4,5],[6,7,8]]

print(rotate_by_90_degrees(matrix))
