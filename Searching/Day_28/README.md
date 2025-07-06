# Problem Statement: Number of Occurence (Easy)
Given a sorted array arr and a target element, find the number of occurence of target in arr.

## Concept:
Binary Search in Arrays.

## Approach:
1. Here we will use binary search two times: one to find first occurence of target element and another to find last occurence of target element.
2. For the first occurence: In binary search, if we get arr[mid]==target: store the index value and check for another occurence in the left-half (end=mid-1).
3. Similarly for the last occurence: In binary search, if we get arr[mid]==target: store the index value and check for another occurence in the right-half (start=mid+1).
4. Number of occurence would be last_occurence-first_occurence+1.

## Time and Space Complexity:
Time Complexity: O(log*N)

Space Complexity: O(1)

## Example:
**Input**: arr=[1,1,2,2,2,2,3]

**Output**: ans=4

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/number-of-occurrence2259
