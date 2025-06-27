# Problem Statement: Maximum Circular Subarray Sum (Hard)
Given an array arr[] in circular fashion, find the maximum sum that we can get from any subarray formed by the array.

## Concept:
Extended Kadane's Algorithm.

## Approach:
1. First traverse through the array and find the total sum of the array. Store it in total_sum.
2. Initialise two variables current_max= 0 and global_max= arr[0]. Traverse through the array and for each element update current_max as maximum of current_max+arr[i] and arr[i]. And for global_max as maximum of current_max and global_max.
3. If global_max<0, it means that all elements in the array are negative. Therefore answer would be global_max.
4. Again initialise two variables current_min= 0 and global_min= arr[0]. Traverse through the array and for each element update current_min as minimum of current_min+arr[i] and arr[i]. And for global_min as minimum of current_min and global_min.
5. Answer would be maximum of global_max and total_sum-global_min (For satisfying circular property of array).

## Time and Space Complexity:
Time Complexity: O(N)+O(N)+O(N)= O(3*N) (It can be optimised and all the calculations can be done in one traversal only)

Space Complexity: O(1)

## Example:
**Input**: arr=[10,-3,-4,7,6,5,-4,-1]

**Output**: max_sum= 23. subarray=[7,6,5,-4,-1,10].

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/max-circular-subarray-sum-1587115620
