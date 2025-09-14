'''
Given a string, return the length of the last word
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = (s.strip(" ")).split(" ")
        return len(lst[-1])
