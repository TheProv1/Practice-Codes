"""
Exponents

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if (-100.0 < x < 100.0):
            y = x ** n
            return float(y)
        
        else:
            return 0
