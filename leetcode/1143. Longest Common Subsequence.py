"""
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none)
deleted without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        R, C = len(text1), len(text2)
        dp = [[0]*(C + 1) for i in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]