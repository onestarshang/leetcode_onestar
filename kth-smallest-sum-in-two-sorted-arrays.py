# coding=utf8

'''
Given two integer arrays sorted in ascending order and an integer k. Define sum
 = a + b, where a is an element from the first array and b is an element from
 the second one. Find the kth smallest sum out of all possible sums.


Example
Given [1, 7, 11] and [2, 4, 6].

For k = 3, return 7.

For k = 4, return 9.

For k = 8, return 15.

'''
# heap

class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        import heapq

        if not A or not B:
            return 0

        length_a, length_b = len(A), len(B)
        heap = []
        for i in range(min(k, length_b)):
            heapq.heappush(heap, (A[0] + B[i], 0, i))

        while k > 1:
            min_value, index_a, index_b = heapq.heappop(heap)
            if index_a + 1 < length_a:
                heapq.heappush(heap, (A[index_a + 1] + B[index_b], index_a + 1, index_b))
            k -= 1
        return heapq.heappop(head)[0]

