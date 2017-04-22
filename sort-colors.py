# coding=utf8

'''
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

# extra place: hash map

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # no extra place

        def swap(nums, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        start, end = 0, len(nums) - 1
        index = 0
        while index <= end:
            if nums[index] == 0:
                swap(nums, index, start)
                index += 1
                start += 1
            elif nums[index] == 1:
                index += 1
            else:
                swap(nums, index, end)
                end -= 1
