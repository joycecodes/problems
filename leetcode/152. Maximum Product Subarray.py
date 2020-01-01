"""
Given an integer array nums,
find the contiguous subarray within an array (containing at least one number) which has the largest product.
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)

        dpmax, dpmin = size * [0], size * [0]
        dpmax[0] = dpmin[0] = nums[0]

        for i in range(1, size):
            a = dpmax[i - 1] * nums[i]
            b = dpmin[i - 1] * nums[i]
            c = nums[i]
            dpmax[i] = max(a, b, c)
            dpmin[i] = min(a, b, c)

        return max(dpmax)