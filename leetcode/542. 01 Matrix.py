"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        x,y = len(matrix), len(matrix[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(x):
            for j in range(y):
                if matrix[i][j] != 0:
                    q = collections.deque([[(i,j)]])
                    visited = [[i,j]]
                    while q:
                        temp = q.popleft()
                        i_2,j_2 = temp[-1][0], temp[-1][1]
                        if (i_2+1 < x and matrix[i_2+1][j_2] == 0)\
                        or (i_2 - 1 >= 0 and matrix[i_2-1][j_2] == 0)\
                        or (j_2 + 1 < y and matrix[i_2][j_2+1] == 0)\
                        or (j_2 - 1 >= 0 and matrix[i_2][j_2-1] == 0):
                            matrix[i][j] = len(temp)
                            break
                        for a,b in directions:
                            if i_2 + a >= 0 and i_2 + a < x and j_2 + b >= 0 and j_2 + b < y:
                                if not (i_2 + a, j_2 + b) in visited:
                                    q.append(temp + [(i_2 + a, b + j_2)])
                                    visited+= [(i_2 + a, b + j_2)]
        return matrix