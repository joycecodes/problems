"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        maze = [[0 for i in range(n)] for i in range(m)]

        for x in range(m):
            maze[x][0] = 1
        for x in range(n):
            maze[0][x] = 1

        for x in range(1, m):
            for y in range(1, n):
                maze[x][y] = maze[x - 1][y] + maze[x][y - 1]

        return maze[-1][-1]