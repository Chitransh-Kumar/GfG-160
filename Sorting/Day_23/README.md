# Problem Statement: Count Inversions (Medium)
Given an array arr[], count the no. of inversions in the array. Two elements arr[i] and arr[j] form an inversion if arr[i]>arr[j] and i<j.

## Concept:
Merge sort.

## Approach:
1. We apply the normal merge sort algorithm in the array where the array is divided into two subarrays until single element array is not reached and then merge the subarrays in ascending order.
2. While merging if element arr[left] (Left subarray) is greater than arr[right] (Right subarray), we increase count by (mid-left+1) which is count of elements in Left subarray greater than arr[right].

## Time and Space Complexity:
Time Complexity: O(N*logN)

Space Complexity: O(N)

## Example:
**Input**: arr=[1,9,3,5,7,8,2,4]

**Output**: ans= 13

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/inversion-of-array-1587115620
