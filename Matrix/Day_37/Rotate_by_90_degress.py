def rotate_by_90_degrees(matrix):
    n=len(matrix)

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(n):
        top=0
        bottom=n-1
        while top<=bottom:
            matrix[top][i],matrix[bottom][i]=matrix[bottom][i],matrix[top][i]    
            top+=1
            bottom-=1

    return matrix
    
matrix=[[0,1,2],[3,4,5],[6,7,8]]

print(rotate_by_90_degrees(matrix))