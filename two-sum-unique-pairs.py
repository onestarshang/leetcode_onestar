# coding=utf8

'''
Given an array of integers, find how many unique pairs in the array such
that their sum is equal to a specific target number. Please return the number of pairs.

Given nums = [1,1,2,45,46,46], target = 47
return 2

1 + 46 = 47
2 + 45 = 47
'''

class Solution:
    # @param nums {int[]} an array of integer
    # @param target {int} an integer
    # @return {int} an integer
    def twoSum6(self, nums, target):
        # Write your code here
        nums.sort()
        start, end = 0, len(nums) - 1
        cnt = 0
        while start < end:
            if nums[start] + nums[end] == target:
                cnt += 1
                start += 1
                end -= 1
                while start < end and nums[start - 1] == nums[start]:
                    start += 1
                while start < end and nums[end] == nums[end + 1]:
                    end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return cnt
