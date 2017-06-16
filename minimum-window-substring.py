# coding=utf8

'''
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the
empty string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.
'''

class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        # write your code here
        if not source or not target:
            return ''

        source_hash = [0] * 256
        target_hash = [0] * 256
        for t in target:
            target_hash[ord(t)] += 1

        import sys
        ans = sys.maxint
        min_str = ''
        left = right = 0

        def valid(source_hash, target_hash):  # source 中有没有 target
            for i in range(256):
                if target_hash[i] > source_hash[i]:
                    return False
            return True

        for left in range(len(source)):
            while not valid(source_hash, target_hash) and right < len(source):
                source_hash[ord(source[right])] += 1
                if right < len(source):
                    right += 1
                else:
                    break

            if valid(source_hash, target_hash):
                if ans > right - left:
                    ans = min(ans, right - left)
                    min_str = source[left: right]

            source_hash[ord(source[left])] -= 1
        return min_str

