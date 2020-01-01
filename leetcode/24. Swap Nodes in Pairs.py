"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = cur = ListNode(0)
        cur.next = head

        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next = b
            a.next = b.next
            b.next = a

            cur = a

        return start.next