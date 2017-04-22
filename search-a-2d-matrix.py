# coding=utf8

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        start, end = 0, m * n -1
        while start + 1 <end:
            mid = start + (end - start) / 2
            row = mid / n     # 除以列数
            col = mid % n     # 模上列数
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid
            else:
                end = mid
        if matrix[start / n][start % n] == target:  # 校验边界
            return True
        elif matrix[end / n][end % n] == target:
            return True
        return False
