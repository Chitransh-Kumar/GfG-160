# Problem Statement: Search in a Row-Column sorted matrix (Easy)
Given a 2D rectangular matrix of size NxM in which each row and each column is sorted in ascending order and a target element x, find whether x is present in the matrix or not.

## Concept:
Matrix traversal.

## Approach:
1. Start from row=0 and col=M-1.
2. If matrix[row][col] equals x: return True.
3. Otherwise if matrix[row][col] greater than x: decrease col (col--).
4. Otherwise if matrix[row][col] less than x: increase row (row++).

## Time and Space Complexity:
Time Complexity: O(N+M)

Space Complexity: O(1)

## Example:
**Input**: mat=[[3,30,38],[20,52,54],[35,60,69]] x=54

**Output**: ans= True.

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-matrix17201720
