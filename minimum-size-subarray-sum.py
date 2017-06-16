# coding=utf8

'''
Given an array of n positive integers and a positive integer s, find the minimal
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        import sys

        if not nums:
            return 0

        left = right = 0
        sum = 0
        ans = sys.maxint

        for left in range(len(nums)):
            while right < len(nums) and sum < s:
                sum += nums[right]
                right += 1
            if sum >= s:
                ans = min(ans, right - left)
            sum -= nums[left]
        if ans == sys.maxint:
            return 0
        return ans
