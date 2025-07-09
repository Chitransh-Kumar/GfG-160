# Problem Statement: Peak Element (Basic)
Given an array arr where no two elements are the same, find whether peak element is present in the array or not. Peak element is the one which is greater than both of its adjacent elements.

## Concept:
Binary Search in Arrays.

## Approach:
1. If arr[0]>arr[1] or arr[n-1]>arr[n-2], return True as it would be the peak element.
2. Otherwise apply Binary Search from start=1 to end=n-2.
3. In Binary Search, if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1], return True.
4. If arr[mid]>arr[mid+1]: move to the left-side of the array (end=mid-1).
5. If arr[mid]>arr[mid-1]: move to the right-side of the array (start=mid+1).

## Time and Space Complexity:
Time Complexity: O(logN)

Space Complexity: O(1)

## Example:
**Input**: arr=[1,2,4,5,7,8,3]

**Output**: ans=8

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/peak-element
