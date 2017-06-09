# coding=utf8

'''
Find the kth smallest number in at row and column sorted matrix.

Example
Given k = 4 and a matrix:

[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
return 5
'''

class Solution:
    # @param matrix: a matrix of integers
    # @param k: an integer
    # @return: the kth smallest number in the matrix
    def kthSmallest(self, matrix, k):
        # write your code here
        import heapq

        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]  # init visited hash

        queue = [(matrix[0][0], 0, 0)]
        result = None
        visited[0][0] = True

        for _ in range(k):
            result, i, j = heapq.heappop(queue)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(queue, (matrix[i + 1][j], i + 1, j))

            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(queue, (matrix[i][j + 1], i, j + 1))
        return result
