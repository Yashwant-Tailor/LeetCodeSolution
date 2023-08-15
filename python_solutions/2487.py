# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def update_link_list(self,curr_node,prev_node):
        if curr_node is None:
            return 0,None
        max_val,next_node = self.update_link_list(curr_node.next,curr_node)
        if max_val > curr_node.val:
            if prev_node is None:
                return max_val,next_node
            else:
                prev_node.next = next_node
                return max_val,next_node
        else:
            max_val = curr_node.val
            return max_val,curr_node

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Solution Overview
        # we use recursion to expand the linked list(traversing the list)
        # then while returning from the recursion we return the maximum value we have encountered in reverse order

        max_val,head = self.update_link_list(head,None)
        return head
