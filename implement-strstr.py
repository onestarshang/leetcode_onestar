# coding=utf8

'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
'''

## 时间复杂度满足 O(m+n)

class Solution(object):
    def strStr(self, source, target):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ## O(m + n)
        #hash function
        if source is None:
            return -1
        if target is None:
            return -1

        m = len(target)
        n = len(source)

        if m == 0:
            return 0

        import sys
        mod = sys.maxint / 31
        hash_target = 0
        m31 = 1

        for i in range(m):
            hash_target = (hash_target * 31 + ord(target[i]) - ord('a')) % mod
            if hash_target < 0:
                hash_target += mod

        for i in range(m - 1):
            m31 = m31 * 31 % mod   ##

        hash_src = 0
        for i in range(n):
            if i >= m:
                hash_src = (hash_src - m31 * (ord(source[i - m]) -  ord('a'))) % mod
            hash_src = (hash_src * 31 + ord(source[i]) - ord('a')) % mod
            if hash_src < 0:
                hash_src += mod
            if i >= m - 1 and hash_src == hash_target:
                return i - m + 1
        return -1
