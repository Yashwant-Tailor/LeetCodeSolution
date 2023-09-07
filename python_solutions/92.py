# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before_left = None
        left_pointer = None
        right_pointer = None
        after_right = None
        tail = None
        curr_head = head
        curr_position = 0
        while curr_head is not None:
            curr_position += 1
            curr_node = curr_head
            curr_head = curr_head.next
            curr_node.next = None
            if curr_position < left:
                if before_left is not None:
                    before_left.next  = curr_node
                before_left = curr_node
            if curr_position == left:
                right_pointer = curr_node
            if left <= curr_position <= right:
                curr_node.next = left_pointer
                left_pointer = curr_node
            if curr_position > right:
                if after_right is None:
                    after_right = curr_node
                else:
                    tail.next = curr_node
                tail = curr_node
        if before_left is None:
            head = left_pointer
        else:
            before_left.next = left_pointer
        right_pointer.next = after_right
        return head
