"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = []
        start, end = 0, len(nums)

        stack.append([[], start])
        res = []

        while stack:
            ans, start = stack.pop()
            res.append(ans)

            for i in range(start, end):
                stack.append((ans + [nums[i]], i + 1))

        return res