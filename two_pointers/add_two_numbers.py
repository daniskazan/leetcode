"""
https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = ""
        y = ""
        while l1 or l2:
            if l1:
                x += str(l1.val)

            if l2:
                y += str(l2.val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        res = []
        res_int = int(x[::-1]) + int(y[::-1])
        while res_int:
            x = res_int % 10
            res.append(x)
            res_int = res_int // 10

        dummy = ListNode()
        curr = dummy
        for i in range(len(res)):
            print("here ", res[i])
            curr.val = res[i]
            curr.next = ListNode(res[i + 1]) if i != len(res) - 1 else None
            curr = curr.next
        return dummy
