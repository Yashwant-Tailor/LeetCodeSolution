# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Solution Overview
        # maintain heap of size k with first node of each linked list
        # now iterate while this heap size is greater than 1
        # every time in our iteration we will pick the current minimum element from our heap
        # and insert the next node to the current element in our heap 
        import heapq as hp
        min_heap = []
        class NODE:
            def __init__(self,val,ListNode):
                self.val = val
                self.curr_node = ListNode
            def __lt__(self,other):
                return self.val <= other.val
        for i in range(len(lists)):
            if lists[i] is not None:
                hp.heappush(min_heap,NODE(lists[i].val,lists[i]))
        head,tail = None,None
        while len(min_heap) > 0:
            curr_heap_node = hp.heappop(min_heap)
            curr_min_elm = curr_heap_node.curr_node
            if head is None:
                head = curr_min_elm
                tail = curr_min_elm
            else:
                tail.next = curr_min_elm
                tail = curr_min_elm
            next_elm  = curr_min_elm.next
            curr_min_elm = None
            if next_elm is not None:
                hp.heappush(min_heap,NODE(next_elm.val,next_elm))
        return head

