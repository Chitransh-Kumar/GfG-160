# Problem Statement: Sorted and Rotated Minimum (Easy)
Given a sorted and rotated array arr of distinct elements, find the minimum in the array.

## Concept:
Binary Search in Arrays.

## Approach:
1. Here we apply the standard binary search from low=0 to high=n-1, but with some modifications.
2. If arr[mid]>=arr[low]: It means the left-half is sorted and the minimum would always be min element between arr[low] and minimum (initialised with INT_MAX)
3. If arr[mid]<arr[low]: It means the right-half is sorted and the minimum would always be min element between arr[mid] and minimum.

## Time and Space Complexity:
Time Complexity: O(log*N)

Space Complexity: O(1)

## Example:
**Input**: arr=[5,6,1,2,3,4]

**Output**: ans=1

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/minimum-element-in-a-sorted-and-rotated-array3611
