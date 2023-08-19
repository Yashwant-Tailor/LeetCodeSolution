class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Solution Overview
        # we can maintain a heap to find the maximum number in the window of size k
        import heapq as hp
        max_heap = []
        class heap_node:
            def __init__(self,node_val,idx):
                self.idx = idx
                self.val = node_val
            def __lt__(self,other):
                return self.val > other.val
        max_arr = []
        for idx,num in enumerate(nums):
            hp.heappush(max_heap,heap_node(num,idx))
            while max_heap[0].idx <= idx-k:
                hp.heappop(max_heap)
            # point to remember this should come after removing the elements
            if idx >= k-1:
                max_arr.append(max_heap[0].val)
        return max_arr
