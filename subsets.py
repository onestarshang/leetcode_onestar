# coding=utf8

'''
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

## DFS
## subset --> stack

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        if len(nums) == 0:
            return [[]]

        def helper(subset, start, res):   # start index to len(nums) - 1
            res.append(list(subset))
            for i in range(start, len(nums)):
                subset.append(nums[i])
                helper(subset, i + 1, res)    # start index + 1
                subset.pop()

        nums.sort()
        res = []
        helper([], 0, res)
        return res
