# Problem Statement: Add Binary Strings (Medium)
Given two binary strings consisting of 0s and 1s, find the resultant after adding these binary strings. The resultant should not have any leading 0s.

## Concept:
String manipulation, two pointers

## Approach:
1. Take two pointers first and second at the last element of s1 and s2 respectively.
2. Initialise carry variable to 0.
3. Traverse through both the strings s1 and s2 till first>=0 and second>=0:
   a. If carry==0:
     1. If s1[first]=='0' and s2[second]=='0': add '0' to ans.
     2. If s1[first]=='0' or s2[second]=='0': add '1' to ans.
     3. If s1[first]=='1' and s2[second]=='1': add '0' to ans and update carry=1.
   b. If carry==1:
     1. If s1[first]=='0' and s2[second]=='0': add '1' to ans and update carry=0.
     2. If s1[first]=='0' or s2[second]=='0': add '0' to ans.
     3. If s1[first]=='1' and s2[second]=='1': add '1' to ans.
4. Now there may be some elements left to traverse either in s1 or s2.
5. Traverse through s1 or s2 (whichever necessary) till first/second>=0:
   a. If carry==0:
     1. If s1[first] or s2[second]=='0': add '0' to ans.
     2. If s1[first] or s2[second]=='1': add '1' to ans.
   b. If carry==1:
     1. If s1[first] or s2[second]=='0': add '1' to ans and update carry=0.
     2. If s1[first] or s2[second]=='1': add '0' to ans.
6. At last, add carry value to ans.
7. Trim down the leading zeros in the answer and return the answer.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(N)

## Example:
**Input**: s1='00100' s2='010'

**Output**: ans='110'

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/add-binary-strings3805
