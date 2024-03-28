# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self,head:Optional[ListNode])->int:
        list_len = 0 
        while head is not None:
            list_len += 1
            head = head.next
        return list_len
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        head2 = head
        list_len  = self.get_len(head)
        skip_node = list_len//2
        cnt = skip_node
        while cnt > 0:
            cnt -= 1
            head2 = head2.next
        if list_len%2 == 1:
            head2 = head2.next
        rev_head = None
        while head2 is not None:
            curr_node = head2
            head2 = head2.next
            curr_node.next = rev_head
            rev_head = curr_node
        
        head2 = rev_head
        new_head = head
        cnt = skip_node
        while cnt > 0:
            cnt -= 1
            curr_head_node = head
            head = head.next
            curr_head2_node = head2
            head2 = head2.next
            curr_head_node.next = curr_head2_node
            curr_head2_node.next = head
        head.next = None
        return new_head
