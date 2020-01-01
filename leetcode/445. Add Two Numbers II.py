"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        cur1 = l1
        cur2 = l2

        while cur1:
            stack1.append(cur1)
            cur1 = cur1.next
        while cur2:
            stack2.append(cur2)
            cur2 = cur2.next

        res = []
        carry = 0

        while stack1 and stack2:
            val = stack1.pop().val + stack2.pop().val + carry

            if val > 9:
                carry = 1
                val = val - 10
            else:
                carry = 0
            res.insert(0, val)

        while stack1:
            val = stack1.pop().val + carry
            if val > 9:
                carry = 1
                val = val - 10
            else:
                carry = 0
            res.insert(0, val)

        while stack2:
            val = stack2.pop().val + carry
            if val > 9:
                carry = 1
                val = val - 10
            else:
                carry = 0
            res.insert(0, val)

        if not stack1 and not stack2 and carry == 1:
            carry = 0
            res.insert(0, 1)

        head = cur = ListNode(res.pop(0))

        while res:
            cur.next = ListNode(res.pop(0))
            cur = cur.next
        return head