# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self,head):
        ans = 0 
        curr_head = head
        while curr_head is not None:
            ans += 1
            curr_head = curr_head.next
        return ans
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        len_lk = self.get_len(head)
        rem = len_lk%k
        part_len = len_lk//k
        curr_head = head
        ans_head = [None for idx in range(k)]
        ans_tail = [None for idx in range(k)]
        part_idx = 0
        while curr_head is not None:
            temp_part_len = part_len
            while temp_part_len > 0 and curr_head is not None:
                temp_part_len -= 1
                temp_node = curr_head
                curr_head = curr_head.next
                temp_node.next = None
                if ans_head[part_idx] is None:
                    ans_head[part_idx] = temp_node
                    ans_tail[part_idx] = temp_node
                else:
                    ans_tail[part_idx].next = temp_node
                    ans_tail[part_idx] = temp_node
            if rem > 0 and curr_head is not None:
                rem -= 1
                temp_node = curr_head
                curr_head = curr_head.next
                temp_node.next = None
                if ans_head[part_idx] is None:
                    ans_head[part_idx] = temp_node
                    ans_tail[part_idx] = temp_node
                else:
                    ans_tail[part_idx].next = temp_node
                    ans_tail[part_idx] = temp_node
            part_idx += 1
        return ans_head
