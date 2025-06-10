# Problem Statement: Reverse an Array (Easy)
Given an array, reverse the array. All the changes should be made in-place only.

## Concept:
Two pointers.

## Approach:
1. Initialise two pointers: first=0 and last=n-1.
2. While first<=last: swap arr[first] and arr[last], first=first+1, last=last-1.

## Time and Space Complexity:
Time Complexity: O(N).

Space Complexity: O(1).

## Example:
**Input**: arr[]=[5,4,3,6,1,9]

**Output**: [9,1,6,3,4,5]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/reverse-an-array
