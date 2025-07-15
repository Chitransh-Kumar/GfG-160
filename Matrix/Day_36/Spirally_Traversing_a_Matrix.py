def spirally_traversing_a_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    left=0
    right=cols-1
    top=0
    bottom=rows-1

    ans=[]
    while top<=bottom and left<=right:
        
        for j in range(left,right+1):
            ans.append(matrix[top][j])
        top+=1

        for i in range(top,bottom+1):
            ans.append(matrix[i][right])
        right-=1

        if top<=bottom:
            for j in range(right,left-1,-1):
                ans.append(matrix[bottom][j])
            bottom-=1

        if left<=right:
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left+=1

    return ans

matrix=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
print(spirally_traversing_a_matrix(matrix))
