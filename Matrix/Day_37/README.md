# Problem Statement: Rotate by 90 degree (Easy)
Given a square matrix of size NxN, rotate the matrix by 90 degrees in anti-clockwise direction.

## Concept:
Matrix.

## Approach:
1. Find the transpose of the matrix.
2. If matrix is to be rotated in anti-clockwise direction, swap row elements for each column.
3. If matrix is to be rotated in clockwise direction, swap column elements foe each row.

## Time and Space Complexity:
Time Complexity: O(N^2)

Space Complexity: O(1)

## Example:
**Input**: mat= [[0,1,2],[3,4,5],[6,7,8]]

**Output**: ans=[[2,5,8],[1,4,7],[0,3,6]]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/rotate-by-90-degree-1587115621
