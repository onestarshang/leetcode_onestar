# coding=utf8

'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        # traverse
        def dfs(root, tmp_sum, sum, res):
            if root.left is None and root.right is None:
                if tmp_sum == sum:
                    res.append(1)
                return
            if root.left:
                dfs(root.left, tmp_sum + root.left.val, sum, res)
            if root.right:
                dfs(root.right, tmp_sum + root.right.val, sum, res)

        res = []
        dfs(root, root.val, sum, res)
        if 1 in res:
            return True
        return False
