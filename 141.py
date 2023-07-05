# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:  # Not good solution because we change values of List
#     def hasCycle(self, head: ListNode) -> bool:
#         while head:
#             if head.val is None:
#                 return True
#             head.val = None
#             head = head.next
#         return False

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # We are going to use slow and fast pointer technique
        slow, fast = head, head
        while fast and fast.next:  # Order is important!
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
