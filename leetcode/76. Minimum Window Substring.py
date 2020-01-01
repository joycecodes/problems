"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}  # key: character, value: number of apperances
        for index, c in enumerate(t):
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1

        total = len(t)  # 3
        left = 0
        res = len(s) + 1
        l = 0
        r = 0
        for right, c in enumerate(s):
            if c in d:  # A
                d[c] = d[c] - 1  # b: 0 -1  t:ab
                if d[c] >= 0:
                    total -= 1  #

            while total == 0:
                if right - left + 1 < res:
                    res = right - left + 1
                    l = left
                    r = right
                if s[left] in d:
                    d[s[left]] = d[s[left]] + 1
                    if d[s[left]] >= 1:
                        total += 1
                left += 1
        if res == len(s) + 1:
            return ""
        else:
            return s[l:r + 1]