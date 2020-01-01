"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right = len(nums) - 1
        left = right - 1
        if len(nums) == 1:
            return True
        while left > 0:
            if nums[left] >= right-left:
                left-=1
                right-=1
            else:
                while nums[left] < right-left and left > 0:
                    left-=1
                if left != 0:
                    right = left
                    left-=1
                if left == 0 and nums[left] < right:
                    return False
        if nums[left] > 0:
            return True
        else:
            return False