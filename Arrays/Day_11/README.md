# Problem Statement: Maximum Product Subarray (Medium)
Given an array arr[] which consists of positive and negative integers as well as 0, find the maximum product of any subarray formed by the array.

## Concept:
Prefix and Suffix product, Linear Traversal of Arrays.

## Approach:
1. Initialise prefix and suffix to 1 and max_product to INT_MIN.
2. Traverse through the array and update prefix= prefix* arr[i] and suffix= suffix* arr[n-1-i].
3. While traversing through the array, if prefix=0, make prefix=1 and if suffix=0, make suffix=1.
4. For each iteration, max_product= maximum between max_product and (maximum of prefix and suffix).

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(1)

## Example:
**Input**: arr=[-2,6,-3,-10,0,2]

**Output**: ans=180

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/maximum-product-subarray3604
