# coding=utf8
'''
Given an array S of n integers, find three integers in S such that the sum
is closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3:
            return -1
        nums.sort()

        best_sum = None
        for i in range(len(nums)):
            start, end = i + 1, len(nums) - 1
            while start < end:
                _sum = nums[i] + nums[start] + nums[end]
                if best_sum is None or abs(_sum - target) < abs(best_sum - target):
                    best_sum = _sum
                if _sum < target:
                    start += 1
                else:
                    end -= 1
        return best_sum
