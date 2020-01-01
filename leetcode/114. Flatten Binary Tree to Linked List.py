"""
Given a binary tree, flatten it to a linked list in-place.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # pre-order traversal

        if root is None:
            return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        root.right = left
        root.left = None

        node = root

        while node.right:
            node = node.right

        node.right = right
        return root