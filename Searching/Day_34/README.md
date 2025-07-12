# Problem Statement: Allocate Minimum Pages (Medium)
Given an array arr which denotes no. of pages in ith book and k representing no. of students. Allocate books to students such that each student receives at least one book and no book is assigned to more than one student. Find the arrangement in such a way that it minimizes the maximum no. of pages assigned to any student.

## Concept: 
Binary Search on Answers

## Approach:
1. First we define student_num function which takes arr and pages as input.
2. Initialise with students=1 and student_pages=0.
3. Traverse through the array and if student_pages+arr[i]<=pages: student_pages+=arr[i], else student_pages=arr[i] and students++.
4. It means that for a given no. of pages find how many students can be allocated the books.
5. In the main function, apply binary search with low=max(arr) and high=sum(arr).
6. For each mid value, check the student_num value: If it is less than or equal to k: ans=mid and go to left-half of the array (high=mid-1).
7. Otherwise go to right-half of the array (low=mid+1).

## Time and Space Complexity:
Time Complexity: O(N*logN)

Space Complexity: O(1)

## Example:
**Input**: arr=[12,34,67,90] k=2

**Output**: ans=113 (minimum no. of maximum pages allocated to each student)

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/searching-gfg-160/problem/allocate-minimum-number-of-pages0937
