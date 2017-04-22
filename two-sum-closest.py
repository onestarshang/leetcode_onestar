# coding=utf8

'''
找到两个数字使得他们和最接近target


nums = [-1, 2, 1, -4],target = 4.

最接近值为 1
'''

class Solution:
    # @param {int[]} nums an integer array
    # @param {int} target an integer
    # @return {int} the difference between the sum and the target
    def twoSumClosest(self, nums, target):
        # Write your code here
        import sys

        if not nums:
            return -1

        nums.sort()
        diff = sys.maxint
        start, end = 0, len(nums) - 1

        while start < end:
            if nums[start] + nums[end] < target:
                diff = min([diff, target - nums[start] - nums[end]])
                start += 1
            else:
                diff = min([diff, nums[start] + nums[end] - target])
                end -= 1
        return diff
