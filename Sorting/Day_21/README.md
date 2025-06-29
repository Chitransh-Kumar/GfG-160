# Problem Statement: Sort 0s, 1s and 2s (Medium)
Given an array arr[] consisting of only 0s, 1s and 2s, sort the array in ascending order without using any built-in functions.

## Concept:
Dutch National Flag algorithm.

## Approach:
1. According to this algorithm, initialise three pointers low, mid and high.
2. Ideally, elements from **start of the array** to **low-1** should be 0, from **low** to **mid-1** should be 1, **high+1** to **end of the array** should be 2 and elements between **mid** and **high** can be 0/1/2, which is to be sorted.
3. Initialise low=0, mid=0 and high=n-1, and loop through the array till mid<=high.
4. If arr[mid]==0: swap arr[low] and arr[mid], and increase low and mid by 1. (low++, mid++)
5. If arr[mid]==1: the element is in right position, just increase mid by 1. (mid++)
6. If arr[mid]==2: swap arr[mid] and arr[high], and decrease high by 1. (high--)

## Time Complexity:
Time Complexity: O(N)

Space Complexity: O(1)

## Example:
**Input**: arr= [0,1,1,0,1,2,1,2,0,0,0,1]

**Output**: ans= [0,0,0,0,0,1,1,1,1,1,2,2]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/sort-an-array-of-0s-1s-and-2s4231
