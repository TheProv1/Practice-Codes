"""
Square Root

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
"""

class Solution:
    def mySqrt(self, x: int) -> int:

        if ((0 <= x) & (x <= (2**31 -1))):
            return int(x**0.5)
        
        else:
            return 0
