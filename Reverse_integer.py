'''
Reverse Integer

Question: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0:
            rev_1_str = str(x)
            rev = ""

            for i in range(len(rev_1_str),0,-1):
                rev = rev + rev_1_str[i-1]
            
            if ((int(rev) >= (-2**31)) and (int(rev) <= (2**31) - 1)):
                return int(rev)
            else:
                return 0

        else:
            
            modified_int = x + (-2 * x)
            rev_1 = str(modified_int)
            rev = ""

            for i in range(len(rev_1),0,-1):
                rev = rev + str(rev_1[i-1])
            
            if ((int(rev) >= (-2**31)) and (int(rev) <= (2**31) - 1)):
                return (int(rev) - (2*int(rev)))
            else:
                return 0
