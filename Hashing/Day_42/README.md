# Problem Statement: Two Sum - Pair with Given Sum (Easy)
Given an array arr and target value, find whether or not two numbers are present in array whose sum is target.

## Concept:
Hashing

## Approach:
1. Traverse through the array and for each element find difference (difference=target-arr[i]).
2. If difference is present in hash_map: return True.
3. Add arr[i] to the hash_map.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(N)

## Example:
**Input**: arr=[0,-1,2,-3,1] target=1

**Output**: ans=True

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/hashing-gfg-160/problem/key-pair5616
