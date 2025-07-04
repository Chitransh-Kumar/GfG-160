# Problem Statement: Non-Overlapping Intervals (Medium)
Given an array of intervals arr, where arr[i]=[start,end]. Find the minimum no. of intervals that is to be removed to make the rest of the intervals non-overlapping.

## Concept:
Linear Traversal of array, Greedy algorithm

## Approach:
1. Here we will find the no. of non-overlapping intervals and the difference between total no. of intervals and non-overlapping intervals will give no. of overlapping intervals.
2. First sort the array based on 1st index element.
3. Initialise non_overlap variable as arr[0][1] and cnt as 1.
4. Traverse from 1st element till the end of the array and if ith element's 0th index> non-overlap: update its value to arr[i][1] and increase the cnt by 1.
5. Difference between total no. of elements (N) and cnt will be the answer.

## Time and Space Complexity:
Time Complexity: O(N*logN)

Space Complexity: O(1)

## Example:
**Input**: arr= [[1,2],[2,3],[3,4],[1,3]]

**Output**: ans= 1  arr=[[1,2],[2,3],[3,4]]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/non-overlapping-intervals
