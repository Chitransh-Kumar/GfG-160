# Problem Statement: Kadane's Algorithm (Medium)
Given an array arr[], find the maximum sum of subarray formed in the array.

## Concept:
Kadane's Algorithm, Linear Traversal in Arrays

## Approach:
1. Initialise sum=0 and max_sum= INT_MIN.
2. Traverse through the array and add sum= sum+arr[i].
3. While traversing, if sum<0, make sum=0 and update max_sum as maximum of sum and max_sum.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(1)

## Example:
**Input**: arr= [2,3,-8,7,-1,2,3]

**Output**: ans=11

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/kadanes-algorithm-1587115620
