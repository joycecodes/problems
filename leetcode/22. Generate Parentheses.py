"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        stack = [["(", 1, 0]]

        while stack:
            string, l, r = stack.pop()
            if l == n and r == n:
                res.append(string)
            if l+1 <= n and r <= l:
                stack.append([string + "(", l+1, r])
            if r+1 <= n and r <= l:
                stack.append([string + ")", l, r+1])
        return res