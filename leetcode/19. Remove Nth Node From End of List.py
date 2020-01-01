"""
Given a linked list, remove the n-th node from the end of list and return its head.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):

        # find length of list:

        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1
        print(length)
        ########

        if length == 1 and n == 1:
            return None
        if n == 1 and length == 2:
            head.next = None
            return head
        elif n == 2 and length == 2:
            temp = head.next
            head.next = None
            head = temp
            return head

        n = length - n

        if n == 0:
            cur = head.next
            head = cur

            while cur:
                cur = cur.next
            return head

        print(n)
        # n points to the item before deleted
        cur = head
        count = 1
        while cur:
            if count != n:
                cur = cur.next
                count += 1
            else:
                cur.next = cur.next.next
                break
        return head