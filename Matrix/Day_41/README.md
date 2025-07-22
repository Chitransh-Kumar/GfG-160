# Problem Statement: Set Matrix Zeros (Medium)
Given a 2D rectangular matrix, modify the matrix such that if mat[i][j]=0, set the entire ith row and jth column to be 0.

## Concept:
Matrix manipulation.

## Approach:
1. Traverse through the matrix and if mat[i][j]==0: set mat[i][0]=0 and mat[0][j]=0 (if j!=0) or col0=0 (if j==0).
2. Now traverse again through the matrix and if mat[i][0]==0 or mat[0][j]==0: set mat[i][j]=0.
3. Now if mat[0][0]==0: set entire 0th-index row to be 0.
4. If col0==0: set entire 0th-index column to be 0.

## Time and Space Complexity:
Time Complexity: O(N*M)

Space Complexity: O(1)

## Example:
**Input** mat=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]

**Output**: ans=[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/set-matrix-zeroes
