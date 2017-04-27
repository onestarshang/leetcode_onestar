# coding=utf8

'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        def dfs(root, path, res):
            if root.left is None and root.right is None:
                res.append('->'.join(list(path)))
            if root.left:
                dfs(root.left, path + [str(root.left.val)], res)
            if root.right:
                dfs(root.right, path + [str(root.right.val)], res)

        res = []
        dfs(root, [str(root.val)], res)
        return res
