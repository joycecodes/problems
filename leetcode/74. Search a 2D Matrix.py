"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        h = len(matrix)
        w = len(matrix[0])
        left = 0
        right = h * w - 1

        while left <= right:
            idx = (left + right) // 2
            pivot_ele = matrix[idx // w][idx % w]
            if pivot_ele == target:
                return True
            if pivot_ele < target:
                left = idx + 1
            if pivot_ele > target:  ####
                right = idx - 1
        return False