"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return
            if grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(grid, i + 1, j)
                dfs(grid, i - 1, j)
                dfs(grid, i, j - 1)
                dfs(grid, i, j + 1)
            return

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    count += 1
        return count