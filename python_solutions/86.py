# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Solution Overview
        # we can maintain pointers for less than , greater than or equal elements
        head_less = None
        tail_less = None
        head_gre_eq = None
        tail_gre_eq = None
        while head is not None:
            curr_node = head
            head = head.next
            curr_node.next = None
            if curr_node.val < x:
                if head_less is None:
                    head_less = curr_node
                    tail_less = curr_node
                else:
                    tail_less.next = curr_node
                    tail_less = curr_node
            else:
                if head_gre_eq is None:
                    head_gre_eq = curr_node
                    tail_gre_eq = curr_node
                else:
                    tail_gre_eq.next = curr_node
                    tail_gre_eq = curr_node
        if tail_less is None:
            return head_gre_eq
        tail_less.next = head_gre_eq
        return head_less
