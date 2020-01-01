"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0

        ans = 0

        while l <= r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if r_max > l_max:
                ans += l_max - height[l]
                l += 1
            elif r_max <= l_max:
                ans += r_max - height[r]
                r -= 1

        return ans



