# coding=utf8

'''
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function,
nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None
        # left, right = 0, 0
        # while right < len(nums): # right fast
        #     if nums[right]:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #     right +=1

        index = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
