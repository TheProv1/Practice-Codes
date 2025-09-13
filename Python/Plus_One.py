'''
Add one to the integer and return the sum in the form of a list
'''


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 0
        for i in digits:
            x *= 10
            x = (x + i)

        x = str(x + 1)
        lst = []

        for i in x:
            lst.append(int(i))

        return lst
