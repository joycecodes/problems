"""
For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False

        if root1.val == root2.val:
            if self.flipEquiv(root1.right, root2.right) and self.flipEquiv(root1.left, root2.left):
                return True
            else:
                return self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)






