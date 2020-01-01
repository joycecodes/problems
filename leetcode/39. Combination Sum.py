"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = {}
        dp[0] = [[]]
        candidates.sort()
        for c in candidates:
            for t in range(c, target + 1):
                if (t-c) in dp:
                    if t not in dp:
                        dp[t] = []
                    for comb_t_m_c in dp[t-c]:
                        dp[t].append(comb_t_m_c + [c])
        return dp[target] if target in dp else []