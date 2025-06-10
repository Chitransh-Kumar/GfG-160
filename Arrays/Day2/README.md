# Problem Statement: Move All Zeros to End (Easy)

Given an array containing non-negative integers, move all the zeros in the array to the right while maintaing the relative order of non-zero elements. All the changes are to be made in-place.

## Concept:
Two pointers.

## Approach:
1. Initialise two pointers: start=0 and end=0.
2. If arr[start]!=0 and arr[end]!=0: start=start+1, end=end+1.
3. If arr[start]!=0 and arr[end]==0: swap arr[start] and arr[end], start=start+1, end=end+1.
4. Repeat the process till start reaches end of array. (start<n)

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(1)

## Example:
**Input**: arr[]=[1,2,0,4,3,0,5,0]

**Output**: [1,2,4,3,5,0,0,0]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751
