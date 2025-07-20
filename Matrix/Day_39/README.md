# Problem Statement: Search in a row-wise sorted matrix (Easy)
Given a rectangular 2D matrix of size NxM in which each row is sorted in increasing order and an element x, find whether x is present in the matrix or not.

## Concept:
Matrix traversal

## Approach:
1. Loop through every row of the matrix and check if matrix[i][0]<=x<=matrix[i][M-1].
2. If true: apply binary search in the row and check for the presence of x.

## Time and Space Complexity:
Time Complexity: O(N*logM)

Space Complexity: O(1)

## Example:
**Input**: matrix=[[3,4,9],[2,5,6],[9,25,27]] x=9

**Output**: ans=True

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-row-wise-sorted-matrix
