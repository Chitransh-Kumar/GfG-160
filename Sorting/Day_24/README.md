# Problem Statement: Merge Overlapping Subintervals (Medium)
Given an array of intervals arr, where arr[i]= [start,end]. Merge all the overlapping subintervals in the array.

## Concept:
Linear traversal in array.

## Approach:
1. First sort the array arr.
2. Take an ans variable and store arr[0] in it.
3. Now start traversing from 1st element to the end of the array and check if: ans[-1][1]>= arr[i][0], ans[-1][1]= maximum of ans[-1][1] and arr[i][1]. Otherwise add arr[i] in ans variable.

## Time and Space Complexity:
Time Complexity: O(N*logN)

Space Complexity: O(1)

## Example:
**Input**: arr=[[1,3],[2,4],[6,8],[9,10]]

**Output**: ans=[[1,4],[6,8],[9,10]]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/overlapping-intervals--170633
