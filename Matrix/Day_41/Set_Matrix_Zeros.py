# 5 1 2 7
# 3 0 5 2
# 1 3 1 5

# 0 0 0 0
# 0 4 5 0
# 0 3 1 0

def set_matrix_zeros(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    col0=1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0

    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0

    if matrix[0][0]==0:
        for i in range(1,cols):
            matrix[0][i]=0
    
    if col0==0:
        for i in range(rows):
            matrix[i][0]=0

    return matrix

matrix=[[5,6,2,-1,5],[1,5,-2,-3,4],[3,3,3,4,6],[-2,5,5,3,4],[0,-2,1,-3,5]]

print(set_matrix_zeros(matrix))