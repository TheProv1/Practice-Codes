"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

Input: x = 4
Output: 2

Input: x = 8
Output: 2

Constraints:

0 <= x <= 231 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:

        if ((0 <= x) & (x <= (2**31 -1))):
            return int(x**0.5)
        
        else:
            return 0
