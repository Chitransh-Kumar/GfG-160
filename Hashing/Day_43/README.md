# Problem Statement: Count pairs with given sum (Easy)
Given an array arr and target, count the no. of pairs whose sum equals target value.

## Concept:
Hashing.

## Approach:
1. Traverse through the array and for each element find difference (difference=target-arr[i])
2. If difference is present in frequency hash map: increase count by frequency[difference].
3. If arr[i] is present in frequency hash map: increase its count by 1.
4. Otherwise initialise it by 1.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(N)

## Example:
**Input**: arr=[1,5,7,-1,5] target=6

**Output**: count=3

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/count-pairs-with-given-sum--150253
