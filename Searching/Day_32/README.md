# Problem Statement: Kth-element of two Arrays (Medium)
Given two sorted arrays arr1 and arr2, find the element at kth position of the combined sorted array.

## Concept:
Two Pointers

## Approach:
1. Get two pointers first and second with initial values as 0.
2. Loop through the two arrays simultaneously till first<N1 (size of arr1) and second<N2 (size of arr2).
3. If arr1[first]<arr2[second]: If cnt (initialised with 0) ==k: return arr1[first], otherwise cnt++ and first++.
4. Otherwise if arr1[first]>arr2[second]: If cnt==k: return arr2[second], otherwise cnt++ and second++.
5. If cnt!=k till now, loop through the remaining elements in arr1 or arr2 (whichever applicable) in similar way.

## Time and Spcae Complexity:
Time Complexity: O(N1+N2)

Space Complexity: O(1)

## Example:
**Input**: arr1=[2,3,6,7,9] arr2=[1,4,8,10] k=5

**Output**: ans=6

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/k-th-element-of-two-sorted-array1317
