"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        T = set(to_delete)

        def dfs(root):
            if root == None:
                return []
            A = dfs(root.left)
            B = dfs(root.right)
            if root.val in T:
                return A + B
            else:
                if len(A) > 0 and root.left == A[-1]:
                    A.pop()
                else:
                    root.left = None
                if len(B) > 0 and root.right == B[-1]:
                    B.pop()
                else:
                    root.right = None
                return A + B + [root]
        return dfs(root)