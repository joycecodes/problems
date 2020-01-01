"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(i, j, word, cur):
            if i >= len(board) or i < 0 or j < 0 or j >=len(board[0]) or (i,j) in visited:
                return False
            if board[i][j] != word[cur]:
                return False
            visited.add((i, j))
            if cur == len(word)-1:
                return True

            if dfs(i - 1, j, word, cur+1) or dfs(i + 1, j, word, cur+1) or dfs(i, j - 1, word, cur+1) or dfs(i, j + 1, word, cur+1):
                return True

            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word, 0):
                        return True
                    visited.clear()
        return False