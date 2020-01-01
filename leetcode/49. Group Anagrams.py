"""
Given an array of strings, group anagrams together.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            n = sorted(word)
            n = "".join(n)
            if n not in h:
                h[n] = []
            h[n].append(word)

        res = []
        for key in h:
            res.append(h[key])
        return res