"""
Given the root of a binary tree,
find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):

        def helper(root, max_, min_):
            if not root:
                return 0
            if root.val < min_:
                min_ = root.val
            if root.val > max_:
                max_ = root.val
            temp = max(abs(root.val - min_), abs(root.val - max_))

            return max(temp, helper(root.left, max_, min_), helper(root.right, max_, min_))

        return helper(root, root.val, root.val)




