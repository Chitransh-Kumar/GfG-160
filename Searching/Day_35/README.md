# Problem Statement: Kth Missing Positive Number in a Sorted Array (Medium)
Given a sorted array arr of positive integers and k, find the Kth missing positive integer in the sorted array.

## Concept: 
Binary Search in Arrays

## Approach:
1. Apply binary search from low=0 to high=n-1.
2. Find mid=(low+high)/2 and missing=arr[mid]-(mid+1).
3. If missing>=k: go to left-half (high=mid-1) otherwise go to right-half (low=mid+1).
4. The final ans would be k+high+1.

## Time and Space Complexity:
Time Complexity: O(log*N)

Space Complexity: O(1)

## Example:
**Input**: arr=[2,3,4,7,11]  k=5

**Output**: ans=9

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/kth-missing-positive-number-in-a-sorted-array
