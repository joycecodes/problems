"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return None
        nums.sort()
        nums = nums[::-1]

        return nums[k - 1]