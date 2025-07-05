# Problem Statement: Merge Without Extra Space (Medium)
Given two arrays arr1 and arr2, merge the two arrays in sorted order without any extra space. The first N elements should be in arr1 and last M elements should be in arr2, where N and M are size of arr1 and arr2 respectively.

## Concept:
Two pointers

## Approach:
1. Take two pointers left and right set at n1-1 and 0 respectively, where n1 is the length of arr1.
2. Traverse through the two arrays till left>=0 and right<n2, where n2 is the length of arr2.
3. If arr1[left]>arr2[right], swap arr1[left] and arr2[right], decrease left by 1 and increase right by 1.
4. If arr1[left]<arr2[right], means every element to left of arr1[left] is smaller, hence break through the loop.
5. Sort arr1 and arr2 after the loop ends.

## Time and Space Complexity:
Time Complexity: O(N1logN1+N2logN2)

Space Complexity: O(N1+N2) [Auxiliary Space]

## Example:
**Input**: arr1=[1,5,9,10,15,20] arr2=[2,3,8,13]

**Output**: arr1=[1,2,3,5,8,9] arr2=[10,13,15,20]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/merge-two-sorted-arrays-1587115620
