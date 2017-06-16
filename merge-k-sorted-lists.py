# coding=utf8

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq

        if not lists:
            return None

        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        dummy = ListNode(-1)
        tail = dummy
        while heap:
            _, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if tail.next:
                heapq.heappush(heap, (tail.next.val, tail.next))
        return dummy.next
