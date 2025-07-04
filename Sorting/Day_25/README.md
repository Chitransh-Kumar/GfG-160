# Problem Statement: Insert Interval (Medium)
Given an array arr, where arr[i]=[start,end], all of its elements are in sorted increasing order. You have to insert a new element newInterval such that the array arr remains sorted.

## Concept:
Linear Traversal of Array, Greedy Algorithm.

## Approach:
1. Start from 0th element and check if newInterval[0]>arr[i][1]: If true, add the element in the ans variable.
2. Now check if newInterval[1]>=arr[i][0]: If true, newInterval[0] will be minimum of newInterval[0] and arr[i][0], and newInterval[1] will be maximum of newInterval[1] and arr[i][1]. 
3. Add newInterval to ans variable and add remaining elements of the array to the ans variable.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(N) [Auxiliary space]

## Example:
**Input**: arr=[[1,3],[4,5],[6,7],[8,10]] newInterval=[5,6]

**Output**: arr=[[1,3],[4,7],[8,10]]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/insert-interval-1666733333
