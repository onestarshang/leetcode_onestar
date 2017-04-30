# coding=utf8

'''
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.

Hints:
If you notice carefully in the flattened tree, each node's right child
points to the next node of a pre-order traversal.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def _flatten(root):
            if not root:
                return None

            last_left = _flatten(root.left)
            last_right = _flatten(root.right)

            if last_left:
                last_left.right = root.right
                root.right = root.left
                root.left = None

            if last_right:
                return last_right
            if last_left:
                return last_left
            return root

        _flatten(root)
