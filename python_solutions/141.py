# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Solution overview
        # we can use Floyd's cycle detection algorithm

        slow_head = head
        fast_head = head
        while fast_head is not None and fast_head.next is not None and fast_head.next.next is not None:
            slow_head = slow_head.next
            fast_head = fast_head.next.next
            if slow_head == fast_head:
                return True
        return False
        
