'''
Sorted List of distinct numbers and target, find the position of the target or find the index where the target can be inserted
'''


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (target in nums):
            return nums.index(target)

        else:
            count = 0
            for i in nums:
                if (target > i):
                    count = count + 1
                    print(count)

            return count
