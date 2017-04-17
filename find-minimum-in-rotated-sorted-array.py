# coding=utf8

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.
'''


## half half

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1

        start, end = 0, len(nums) -1
        target = nums[end]

        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                end = mid
            else:
                start = mid

        return min([nums[start], nums[end]])
