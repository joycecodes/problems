import collections

class Queue:
    def __init__(self):
        self.array = []

    def enqueue(self, item):
        self.array.insert(0, item)

    def dequeue(self):
        if self.array != []:
            return self.array.pop()

    def peek(self):
        return self.array[-1].value

    def size(self):
        return len(self.array)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, type):
        if type == "preorder_print":
            return self.preorder_print(self.root, "")
        if type == "inorder_print":
            return self.inorder_print(self.root, "")
        if type == "postorder_print":
            return self.postorder_print(self.root, "")
        if type == "BFS":
            return self.BFS(self.root)

    def preorder_print(self, start, traversal):
        # Root>left>right
        # DFS
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def BFS(self, start):
        if start:
            queue = Queue()
            queue.enqueue(start)

            traversal = ""
            while queue.size() > 0:
                traversal += str(queue.peek()) + "-"
                node = queue.dequeue()

                if node.left:
                    queue.enqueue(node.left)
                if node.right:
                    queue.enqueue(node.right)
            return traversal

    def findBottomLeftValue(self, start):
        if start:
            q = collections.deque()
            q.append(start)
        leftmost = start
        while q:
            for x in range(0, len(q)):
                node = q.popleft()
                if x == 0:
                    leftmost = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return leftmost.value

    # find height of tree
    def maxDepth(self, start):
        if not start:
            return 0
        left = self.maxDepth(start.left) + 1
        right = self.maxDepth(start.right) + 1
        return max(left, right)

#           1
#         /   \
#       2       3
#     /   \   /   \
#   4      5 6     7
#
#
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("BFS: ", tree.print_tree("BFS"))
print("inorder: ", tree.print_tree("inorder_print"))
print("postorder: ", tree.print_tree("postorder_print"))

