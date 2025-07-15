# Problem Statement: Spirally traversing a matrix (Medium)
Given a rectangular matrix of size NxM, return the traversal of matrix in spiral order.

## Concept:
Matrix traversal.

## Approach:
1. Get four pointers left= 0, right= M-1, top= 0 and bottom= N-1.
2. In the 1st traversal, print all the elements in the row pointed by top, i.e. mat[top][j]. Increment top (top++).
3. In the 2nd traversal, print all the elements in the column pointed by right, i.e. mat[i][right]. Decrement right (right--).
4. In the 3rd traversal, print all the elements in the row pointed by bottom, i.e. mat[bottom][j]. Decrement bottom (bottom--).
5. In the 4th traversal, print all the elements in the column pointed by left, i.e. mat[i][left]. Increment left (left++).
6. Repeat the four traversal till top<=bottom and left<=right.

## Time and Space Complexity:
Time Complexity: O(N*M)

Space Complexity: O(N*M) [Auxiliary Space]

## Example:
**Input**: mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

**Output**: ans=[1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/spirally-traversing-a-matrix-1587115621
