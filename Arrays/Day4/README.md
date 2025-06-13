#  Problem Statement: Rotate Array (Medium)
Given an array and a positive integer d, rotate the array by d places to the left. All the changes are to be done in-place only.

## Concept:
Array Traversal

## Approach: 
1. Initialise a temporary array **temp** with initially all values 0.
2. For the first d elements in the array, copy the elements of the array in **temp** array as temp[i]=arr[i].
3. For the remaining n-d elements, traverse through the array as arr[i-d]=arr[i].
   Eg. arr[2-2]=arr[arr[2], arr[3-2]=arr[3], and so on.
4. For the last d places in the array, copy the elements from **temp** array as arr[n-d+i]=temp[i]/
   Eg. arr[5-2+0]=temp[0], arr[5-2+1]=temp[1], and so on.

## Time and Space Complexity:
Time Complexity: O(d)+ O(n-d)+ O(d)= O(n+d)

Space Complexity: O(d)

## Example: 
Input: arr= [1,2,3,4,5] d=2

Output: [3,4,5,1,2]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/rotate-array-by-n-elements-1587115621
