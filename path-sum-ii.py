# coding=utf8

'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []

        def dfs(root, path, tmp_sum, sum, res):
            if root.left is None and root.right is None:
                if tmp_sum == sum:
                    res.append(list(path))
                return
            if root.left:
                dfs(root.left, path + [root.left.val], tmp_sum + root.left.val, sum, res)
            if root.right:
                dfs(root.right, path + [root.right.val], tmp_sum + root.right.val, sum, res)

        res = []
        dfs(root, [root.val], root.val, sum, res)
        return res
