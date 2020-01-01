"""
Given a string, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        l = r = 0
        count = -1
        while r < len(s):
            if s[r] not in h or h[s[r]] < l:
                h[s[r]] = r
            else:
                count = max(count, (r - l))
                l = h.get(s[r]) + 1
                h[s[r]] = r
            r += 1
        count = max(count, (r-l))
        return count
