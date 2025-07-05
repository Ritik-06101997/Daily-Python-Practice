# Daily-Python-Practice
'''1. Alternates in an Array
Difficulty: BasicAccuracy: 52.74%Submissions: 204K+Points: 1Average Time: 15m
You are given an array arr[], the task is to return a list elements of arr in alternate order (starting from index 0).

Examples:

Input: arr[] = [1, 2, 3, 4]
Output: 1 3
Explanation:
Take first element: 1
Skip second element: 2
Take third element: 3
Skip fourth element: 4
---------------------------
'''
class Solution:
    def getAlternates(self, arr):
        # Code Here
        output =[]
        for i in range(len(arr)):
            if i % 2==0:
                output.append(arr[i])
            else: 
                continue
        return output
    
'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Replace all 0's with 5
Difficulty: BasicAccuracy: 75.55%Submissions: 93K+Points: 1Average Time: 15m
You are given an integer n. You need to convert all zeroes of n to 5.

Examples:

Input: n = 1004
Output: 1554
Explanation: There are two zeroes in 1004 on replacing all zeroes with 5, the new number will be 1554.
Input: n = 121
Output: 121
Explanation: Since there are no zeroes in 121, the number remains as 121.
# Function should return an integer value
'''
class Solution:
    def convertFive(self, n):
        # Code here
        strn = str(n)
        res = ''
        for char in strn:
            if char == '0':
                res = res + '5'
            else:
                res += char
        return res

