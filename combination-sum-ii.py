# coding=utf8

'''
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if i != start and candidates[i] == candidates[i - 1]:
                    continue
                if target < candidates[i]:
                    return
                dfs(candidates, target - candidates[i], i + 1, combination + [candidates[i]], res)

        candidates.sort()
        res = []
        dfs(candidates, target, 0, [], res)
        return res
