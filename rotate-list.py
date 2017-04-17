# coding=utf8

'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = self.list_length(head)
        k = k % length

        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        tail = dummy
        for i in range(k):
            head = head.next

        while head.next:
            tail = tail.next
            head = head.next

        head.next = dummy.next
        dummy.next = tail.next
        tail.next = None
        return dummy.next


    def list_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
