# Problem Statement: Smallest Positive Missing (Medium)
Given an array arr[] consisting of both positive and negative numbers, find the smallest positive missing number. Positive number starts from 1.

## Concept: 
Count sort.

## Approach:
1. In count sort, we sort the array according to the index of array.
2. Traverse through the array and check if the element is in range of 1 to N. If it is true and the element is not in its correct index (arr[i]!=arr[arr[i]-1]), swap the element to its correct index.
3. Do the swapping till arr[i] is not in its correct index or arr[i] is not in range of 1 to N.
4. Once the whole traversal is done, traverse again through the array and check the first element which is not in its correct position. That is the answer.

## Time and Space Complexity:
Time Complexity: O(N)+ O(N)= O(2*N)

Space Complexity: O(1)

## Example:
**Input**: arr=[2,-3,4,1,1,7]

**Output**: ans=3

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/smallest-positive-missing-number-1587115621
