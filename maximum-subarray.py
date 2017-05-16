# coding=utf8

'''
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

# prefix sum

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        import sys
        _max = -sys.maxint
        min_sum = 0
        sum = 0
        for num in nums:
            sum += num
            _max = max([_max, sum - min_sum])
            min_sum = min([sum, min_sum])
        return _max
