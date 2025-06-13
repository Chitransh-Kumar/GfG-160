# Problem Statement: Majority Element 2 (Medium)
Given an array arr, find the element which appears more than N/3 times in the array, where N is the size of the array. If there is no majority element present, return an empty array.

## Concept:
Moore's Voting Algorithm

## Approach:
1. Initialise two variables **count_1** and **count_2** and initialise **element_1** and **element_2** to be INT_MIN.
2. Traverse the array and if count_1 equals 0 and arr[i] is not element_1, set element_1=arr[i] and count_1++. Do the same for element_2.
3. Now if arr[i] equals element_1 or element_2, increase count_1 or count_2 accordingly.
4. If any other element is encountered which is not equal to element_1 or element_2, decrease count_1 or count_2 accordingly.
5. Now cross-check for element_1 and element_2 respectively whether its count in the array is greater than N/3 or not.

## Time and Space Complexity:
Time Complexity: O(N)+ O(N)+ O(N) = O(3*N) 

Space Complexity: O(1)

## Example: 
Input: arr= [2,1,5,5,5,5,6,6,6,6]

Output: [5,6]

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/majority-vote
