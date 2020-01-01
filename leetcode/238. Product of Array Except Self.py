"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [None] * len(nums)
        left[0] = 1

        right = [None] * len(nums)
        right[len(nums) - 1] = 1

        for x in range(1, len(nums)):
            left[x] = left[x - 1] * nums[x - 1]

        for x in range(len(nums) - 2, -1, -1):
            right[x] = right[x + 1] * nums[x + 1]

        for x in range(0, len(nums)):
            nums[x] = left[x] * right[x]

        return nums