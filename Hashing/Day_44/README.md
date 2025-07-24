# Problem Statement: Find All Triplets with Zero Sum (Medium)
Given an array arr, find all the possible triplets whose sum equals zero.

## Concept:
Hashing.

## Approach:
1. Initialise two loops: one outer loop from 0 to n-1 and one inner loop from j+1 (next element) to n-1.
2. For each jth and kth element, find difference=-(arr[j]+arr[k]).
3. If difference is present in hash_map: add it in ans variable.
4. Otherwise add j in the hash_mao.

## Time and Space Complexity:
Time Complexity: O(N**2)

Space Complexity: O(N**2)

## Example:
**Input**: arr=[1,-2,1,0,5]

**Output**: ans=[0,1,2]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/find-all-triplets-with-zero-sum
