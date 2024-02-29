class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_lst = nums1 + nums2
        new_lst.sort()

        length_lst = len(new_lst)

        if (length_lst % 2 == 0):
            get_ind = (length_lst - 1) / 2
            median = (new_lst[int(get_ind)] + new_lst[int(get_ind) + 1]) / 2

            return median
        
        else:
            median = int((length_lst) / 2)
            return new_lst[median]
