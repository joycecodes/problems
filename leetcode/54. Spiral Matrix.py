"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        i = j = 0
        bound_l = bound_u = 0
        bound_r = len(matrix[0])
        bound_d = len(matrix)
        res = []

        while i < len(matrix) and j < len(matrix[0]) and matrix[i][j] not in res:
            while j < bound_r and matrix[i][j] not in res:
                res.append(matrix[i][j])
                j += 1
            bound_r -= 1
            j -= 1
            i +=1
            while i < bound_d and matrix[i][j] not in res:
                res.append(matrix[i][j])
                i += 1
            bound_d -= 1
            i-=1
            j-=1
            while j >= bound_l and matrix[i][j] not in res:
                res.append(matrix[i][j])
                j -= 1
            bound_l += 1
            j += 1
            i-=1
            while i > bound_u and matrix[i][j] not in res:
                res.append(matrix[i][j])
                i -= 1
            i += 1
            j+=1
            bound_u +=1
        return res