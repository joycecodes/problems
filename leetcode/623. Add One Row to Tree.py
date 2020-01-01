"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d.
The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree of the new left subtree root,
its original right subtree should be the right subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all,
then create a tree node with value v as the new root of the whole original tree,
and the original tree is the new root's left subtree.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if (d == 1):
            node = TreeNode(v)
            node.left = root
            return node

        q = collections.deque()
        q.append([root, 2])

        while q:
            node, level = q.popleft()
            if d == level:
                temp, temp2 = node.left, node.right
                node.left = TreeNode(v)
                node.left.left = temp

                node.right = TreeNode(v)
                node.right.right = temp2

            if node.left:
                q.append([node.left, level + 1])
            if node.right:
                q.append([node.right, level + 1])

        return root