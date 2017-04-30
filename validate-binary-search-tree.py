# coding=utf8

'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys

        def validate(root):
            if not root:
                return True, -sys.maxint - 1, sys.maxint

            is_bst_left, max_val_left, min_val_left = validate(root.left)
            is_bst_right, max_val_right, min_val_right = validate(root.right)

            if is_bst_left is False or is_bst_right is False:
                return False, 0, 0
            if (root.left and max_val_left >= root.val) or (root.right and min_val_right <= root.val):
                return False, 0, 0
            return True, max([root.val, max_val_right]), min([root.val, min_val_left])

        is_bst, l, r = validate(root)
        return is_bst
