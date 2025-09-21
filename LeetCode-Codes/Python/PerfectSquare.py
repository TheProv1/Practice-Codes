"""
Perfect Square

Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if (1 <= num <= (2**31)-1):

            x = int(num ** 0.5)

            if ((x**2) == num):
                return True
            
            else:
                False
