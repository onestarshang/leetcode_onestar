# coding=utf8

'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the
root node down to the nearest leaf node.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        import sys

        def get_min(root):
            if not root:
                return sys.maxint
            if root.left is None and root.right is None:
                return 1
            return min([get_min(root.left), get_min(root.right)]) + 1

        return get_min(root)
