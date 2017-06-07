# coding=utf8

'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer
must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        ans = 0
        i = j = 0
        hash_map = {}

        for i in range(len(s)):
            while j < len(s) and hash_map.get(s[j], 0) == 0:
                hash_map[s[j]] = 1
                ans = max(j - i + 1, ans)
                j += 1
            hash_map[s[i]] = 0
        return ans
