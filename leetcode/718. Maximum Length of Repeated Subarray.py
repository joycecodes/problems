"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
"""

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        res = 0
        R, C = len(A), len(B)
        dp = [[0]*(C + 1) for i in range(R + 1)]
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
                res = max(res, dp[i][j])
        return res