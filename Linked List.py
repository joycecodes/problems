class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = Node(node)
        else:
            new_node = Node(node)
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def delete(self, target):
        target = Node(target)
        cur = self.head
        if self.head == None:
            return False
        if target.name == self.head.name:
            self.head = cur.next
            return True
        while cur.next:
            if cur.next.name != target.name:
                cur = cur.next
            else:
                cur.next = cur.next.next
                return True
        return False

    def swap(self, node1, node2):
        prev1 = None
        cur1 = self.head

        if node1 == node2:
            return True

        while cur1 and cur1.name != node1:
            prev1 = cur1
            cur1 = cur1.next

        prev2 = None
        cur2 = self.head
        while cur2 and cur2.name != node2:
            prev2 = cur2
            cur2 = cur2.next

        if (cur1 or cur2) == None:
            return False
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        cur1.next, cur2.next = cur2.next, cur1.next
        return self.print_list()


list = LinkedList()
list.append("A")
list.append("B")
list.append("C")
list.append("D")
list.reverse()
print(list.delete("w"))
print(list.print_list())
