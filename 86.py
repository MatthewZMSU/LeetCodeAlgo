from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_x, greater_eq_x = ListNode(), ListNode()
        new_head, new_tail = less_x, greater_eq_x
        while head is not None:
            if head.val < x:
                less_x.next = head
                less_x = less_x.next
            else:
                greater_eq_x.next = head
                greater_eq_x = greater_eq_x.next
            head = head.next
        greater_eq_x.next = None
        less_x.next = new_tail.next
        return new_head.next
