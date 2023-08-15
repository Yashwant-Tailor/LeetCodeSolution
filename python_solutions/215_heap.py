class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # we can maintain a heap of size k and we will iterate over the array to find the kth largest element in the array
        import heapq as hp
        min_heap = []
        for num in nums:
            hp.heappush(min_heap,num)
            if len(min_heap) == k+1:
                hp.heappop(min_heap)
        return min_heap[0]
