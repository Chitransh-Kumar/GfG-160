# Problem Statement: Implement Atoi (Medium)
Given a string, convert it to an integer without using any built-in functions. Following conditions are to be followed:

1. Ignore the leading whitespaces.
2. Check for '+' or '-', if no sign consider poisitve number.
3. Ignore the leading zeros and read till a non-digit character appears.
4. If the integer is greater than 2^31-1, return 2^31-1 and if integer is less than -2^31, return -2^31.

## Concept:
Strings.

## Approach:
1. Take two boolean variables flag and started and initialise it with False.
2. Traverse through the array and check for one of the following conditions:
   a. If s[i]==' ' and started==False: continue.
   b. If s[i]=='-' and started==False: flag=True and started=True.
   c. If s[i].isdigit(): started=True, num=ord(s[i])-ord('0'), and ans=ans*10+num
   d. Else: break from the loop.
3. If flag==True: ans=-ans
4. If ans>2^31-1: return 2^31-1.
5. If ans<-2^31: return -2^31.
6. Otherwise return ans.

## Time and Space Complexity:
Time Complexity: O(N)

Space Complexity: O(1)

## Example:
**Input**: s='   -0053ivne'

**Output**: ans=-53

## Problem Link:
https://www.geeksforgeeks.org/batch/gfg-160-problems/track/string-gfg-160/problem/implement-atoi
