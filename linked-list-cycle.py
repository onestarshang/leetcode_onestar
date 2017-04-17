# coding=utf8

'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
'''

## extra space  ==>  hashmap
## none extra space solution : fast slow pointer

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        fast = head.next
        slow = head
        while fast!=slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
