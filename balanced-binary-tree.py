# coding=utf8

'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary
tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def _is_balanced(root):
            if not root:
                return True, 0

            is_bal_left, left_depth = _is_balanced(root.left)
            is_bal_right, right_depth = _is_balanced(root.right)

            if is_bal_left is False or is_bal_right is False:
                return False, -1
            if abs(left_depth - right_depth) > 1:
                return False, -1
            return True, max([left_depth, right_depth]) + 1

        is_balanced, _ = _is_balanced(root)
        return is_balanced
