# coding=utf8

'''
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        self.copy_next(head)
        self.copy_random(head)
        return self.split_list(head)

    def copy_next(self, head):
        while head:
            new_node = RandomListNode(head.label)
            new_node.random = head.random
            new_node.next = head.next
            head.next = new_node
            head = head.next.next

    def copy_random(self, head):
        while head:
            if head.next.random:
                head.next.random = head.random.next
            head = head.next.next

    def split_list(self, head):
        dummy = head.next
        while head:
            temp = head.next
            head.next = temp.next
            head = head.next
            if temp.next:
                temp.next = temp.next.next
        return dummy
