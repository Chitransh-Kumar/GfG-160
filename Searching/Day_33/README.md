# Problem Statement: Aggressive Cows (Medium)
Given an array arr which denote position of stall and an integer k which denotes no. of cows, assign cows to stalls such that the minimum distance between two stalls is the maximum possible.

## Concept: 
Binary Search on Answers

## Approach:
1. First define a function can_be_placed which takes N cows, arr and distance d as input.
2. Start with cows_num=1 and last_cow=arr[0] (1st cow should be placed at 0th index).
3. Traverse through the array and if arr[i]-last_cow>=d: last_cow=arr[i] and cows_num++ (It means the distance between two cows cannot exceed d value).
4. Also in each if condition check if cows_num==N: return True
5. In the main function, first sort the array and then apply binary search from start=arr[0] and end=arr[n-1]-arr[0].
6. For each mid value, check if can_be_placed function returns True: store ans=mid and go to the right-half (start=mid+1).
7. If can_be_placed returns False: go to the left-half (end=mid-1).

## Time and Space Complexity:
Time Complexity: O(N*logN)

Space Complexity: O(1)

## Example:
**Input**: arr=[1,2,4,8,9] k=3

**Output**: ans=3 (maximum possible minimum distance between two cows)

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/aggressive-cows
