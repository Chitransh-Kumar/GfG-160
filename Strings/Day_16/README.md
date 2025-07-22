# Problem Statement: Anagram (Easy)
Given two strings s1 and s2, check whether these are anagrams or not. Two words are anagram if they have the same characters with the same frequencies.

## Concept:
Strings, Hashing.

## Appraoch:
1. Create a hash_array of frequencies of size 26.
2. Add the frequency of each character of s1 in hash_array.
3. Now for each character in s2, decrease the frequency by 1.
4. Traverse through the hash_array and check if any element is non-zero, if True return False.

## Time and Space Complexity:
Time Complexity: O(N+M)

Space Complexity: O(1)

## Example:
**Input**: s1="listen"  s2="silent"

**Output**: ans=True.

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/anagram-1587115620
