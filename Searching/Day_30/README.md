# Problem Statement: Search in Rotated Sorted Array (Medium)
Given an array arr which is sorted and rotated, find the target element in the array. If not present, return -1.

## Concept: 
Binary Search in Arrays

## Approach:
1. Apply Binary Search from arr[0] to arr[N-1].
2. If arr[mid]==target, return mid.
3. If arr[low]<=arr[mid]: It means left-half is sorted, if target is between arr[low] and arr[mid], move to left-half (high=mid-1), otherwise move to right-half (low=mid+1).
4. If arr[low]>arr[mid]: It means right-half is sorted, if target is between arr[mid] and arr[high], move to right-half (low=mid+1), otherwise move to left-half (high=mid-1).

## Time and Space Complexity:
Time complexity: O(log*N)

Space complexity: O(1)

## Example:
**Input**: arr=[5,6,7,8,9,10,1,2,3] target=3

**Output**: ans=8

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/search-in-a-rotated-array4618
