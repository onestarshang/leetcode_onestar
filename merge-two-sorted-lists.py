# coding=utf8

'''
Merge two sorted linked lists and return it as a new list. The new list
should be made by splicing together the nodes of the first two lists.
'''


## the key idea : dummy node


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        lastnode = dummy

        while l1 and l2:
            if l1.val < l2.val:
                lastnode.next = l1
                l1 = l1.next
            else:
                lastnode.next = l2
                l2 = l2.next
            lastnode = lastnode.next
        if l1:
            lastnode.next = l1
        elif l2:
            lastnode.next = l2
        return dummy.next
