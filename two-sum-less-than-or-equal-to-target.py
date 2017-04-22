# coding=utf8

'''
Given an array of integers, find how many pairs in the array such that their
sum is less than or equal to a specific target number. Please return the number of pairs.


Given nums = [2, 7, 11, 15], target = 24.
Return 5.
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
'''

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum5(self, nums, target):
        # Write your code here
        if not nums:
            return 0
        nums.sort()

        cnt = 0
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] + nums[end] <= target:
                cnt += (end - start)
                start += 1
            else:
                end -= 1
        return cnt
