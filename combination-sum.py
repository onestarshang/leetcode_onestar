# coding=utf8

'''
Given a set of candidate numbers (C) (without duplicates) and a target
number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
  [7],
  [2, 2, 3]
]
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        def dfs(candidates, target, start, combination, res):
            if target == 0:
                res.append(list(combination))
            for i in range(start, len(candidates)):
                if target < candidates[i]:
                    return
                dfs(candidates, target - candidates[i], i, combination + [candidates[i]], res)

        candidates.sort()
        res = []
        dfs(candidates, target, 0, [], res)
        return res
