"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):

        def helper(node, parent):
            if node:
                node.parent = parent
                helper(node.left, node)
                helper(node.right, node)

        helper(root, None)

        q = collections.deque([[target, 0]])  # add level
        visited = set()
        visited.add(target)

        while q:
            if q[0][1] == K:
                res = []
                for node in q:
                    res.append(node[0].val)
                return res

            node, dis = q.popleft()

            for n in (node.left, node.right, node.parent):
                if n and n not in visited:
                    q.append([n, dis + 1])
                    visited.add(n)

        return []






