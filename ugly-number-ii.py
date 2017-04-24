# coding=utf8

'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''


## 利用 heap + hashmap

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        import heapq
        if n <= 1:
            return n

        n -= 1
        key = [2, 3, 5]
        h = []
        for i in range(3):
            heapq.heappush(h, (key[i], i))

        value = key[0]
        while n > 0:
            value, level = heapq.heappop(h)
            while level < 3:
                new_value = key[level] * value
                heapq.heappush(h, (new_value, level))
                level += 1
            n -= 1
        return value
