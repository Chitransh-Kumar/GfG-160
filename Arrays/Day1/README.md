# Problem Statement: Second Largest (Easy)
Given an array arr[], find the second largest element in the array. If the second largest element does not exist, return -1. Given that array contains only positive integers.

## Concept:
Linear Traversal in Arrays.

## Approach:
1. First, we need to find the largest element in the array.
2. Initialise maximum=-1. Iterate through the array to check if arr[i]>maximum.
3. After finding the maximum, initialise second_maximum=-1.
4. Iterate through the array to check if arr[i]>second_maximum and arr[i]!=maximum.

## Time and Space Complexity:
Time Complexity: O(2*N)

Space Complexity: O(1)

## Example:
**Input**: arr[]=[12,35,1,10,34,1]

**Output**: 34

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/second-largest3735
