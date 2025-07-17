# Problem Statement: Find H-index
Given an array arr, where arr[i] represents no. of citations for ith paper, find the H-index of the researcher. H-index means maximum H value for which researcher has atleast H papers with H citations each.

## Concept:
Count sort

## Approach:
1. Make another array named paper_counts with size N+1 and initialise every element to 0.
2. Traverse through the array and if arr[i]<N: paper_counts[arr[i]]++ otherwise paper_counts[n]++.
3. Traverse backwards from paper_counts array and update papers=papers + paper_counts[i] (initialised with 0). If papers>=i: return i.
4. If through end of loop, nothing is returned: return 0.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(N)

## Example:
**Input**: arr=[3,0,5,3,0]

**Output**: ans= 3

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/sorting-gfg-160/problem/find-h-index--165609
