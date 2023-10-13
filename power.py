"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (-100.0 < x < 100.0):
            y = x ** n
            return float(y)
        
        else:
            return 0
