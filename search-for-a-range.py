# coding=utf8

'''
Given an array of integers sorted in ascending order, find the starting
and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        res = [-1, -1]

        # left bound
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            res[0] = start
        elif nums[end] == target:
            res[0] = end
        else:
            return res

        # right
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            res[1] = end
        elif nums[start] == target:
            res[1] = start
        else:
            return res
        return res
