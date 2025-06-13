# Problem Statement: Next Permutation (Medium)
Given an array of integers, find the next greater lexicographical permutation of integers. If no such permutation exists, find the lowest possible order of the given integers.

## Concept:
Array Traversal

## Approach: 
1. Every array given has a **transition point**. When traversed from the last element in the array, there is a point where the ith element is less than its next (i+1)th element. Find the **transition point**.
2. To find the **transition point**, traverse from the second last element and check if arr[i]<arr[i+1]: if True store index value in index_1 variable (initialised with -1).
3. If index_1 remains -1 after the traversal, it means that the next permutation would be lowest possible order. Reverse the array and return the elements.
4. Find another index_2 which has the index of the element when traversed from the last element, it stores greater value element than value indicated at index_1.
5. To find this, traverse from the last element, with the condition arr[i]>arr[index_1]. Store index_2.
6. Swap arr[index_1] and arr[index_2].
7. Reverse all the elements from the last element till index_1+1 element. The resultant array is the next permutation.

## Time and Space Complexity:
Time Complexity: O(N)+ O(N)+ O(N)= O(3*N).

Space Complexity: O(1).

## Example: 
Input: arr=[2,4,1,7,5,0]

Output: [2,4,5,0,1,7]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/next-permutation5226
