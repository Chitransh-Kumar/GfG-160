# Problem Statement: Search in a Sorted Matrix (Medium)
Given a 2D rectangular matrix of size NxM which is sorted in ascending order, meaning first element of ith row is greater than last element of (i-1)th row, check whether a number x is present in the matrix or not.

## Concept:
Matrix traversal.

## Approach:
1. Think of the 2D matrix as 1D array of N*M size. Apply binary search on the (imagined) array with start=0 and end=NxM-1.
2. Find the mid value and calculate corresponding row and col value according to the formula: row=mid//M and col=row%col.
3. If mat[row][col]==x: return True.
4. If mat[row][col]>x: move to the left-half (end=mid-1).
5. If mat[row][col]<x: move to the right-half (start=mid+1).

## Time and Space Complexity:
Time Complexity: O(log(N*M))

Space Complexity: O(1)

## Example:
**Input**: mat=[[1,5,9],[14,20,21],[34,39,53]] x=34

**Output**: ans=True

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/matrix-gfg-160/problem/search-in-a-matrix-1587115621
