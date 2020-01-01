"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return None

        q = collections.deque()
        q.append(root)
        res = []
        while q:
            l = len(q)
            for x in range(l):
                n = q.popleft()
                if x == l - 1:
                    res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

        return res



