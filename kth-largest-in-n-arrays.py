
# coding=utf8

'''
Find K-th largest element in N arrays.

 Notice

You can swap elements in the array
'''


# heap


class Node:

    def __init__(self, _v, _id, _i):
        self.value = _v
        self.from_id = _id
        self.index = _i

    def __cmp__(self, obj):
        return cmp(obj.value, self.value)

import heapq

class Solution:
    # @param {int[][]} arrays a list of array
    # @param {int} k an integer
    # @return {int} an integer, K-th largest element in N arrays
    @classmethod
    def KthInArrays(self, arrays, k):
        # Write your code here
        # import heapq
        # if not arrays:
        #     return -1

        # h = []
        # heapq.heapify(h)
        # for array in arrays:
        #     array.sort()
        #     h.extend(array[-k:])
        #     h = heapq.nlargest(k, h)
        # if len(h) == k:
        #     return h[-1]
        # return -1
        queue = []
        heapq.heapify(queue)
        for i, array in enumerate(arrays):
            from_id = i
            index = len(array) - 1
            array.sort()
            if index >= 0:
                value = arrays[i][index]
                heapq.heappush(queue, Node(value, from_id, index))


        for i in xrange(k):
            node = heapq.heappop(queue)
            value = node.value
            from_id = node.from_id
            index = node.index

            if i == k-1:
                return value

            if index:
                index -= 1
                value = arrays[from_id][index]
                heapq.heappush(queue, Node(value, from_id, index))

if __name__ == '__main__':
    f = Solution.KthInArrays
    arrays, k = [[2,3,1,5,3], [8, 2, 7, 3, 9]], 3
    print f(arrays, k)

    node1 = Node(4, 0, 2)
    node2 = Node(2, 0, 3)
    print node1 > node2
