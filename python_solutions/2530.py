class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # just maintain a heap and greedily pick the largest element and push it back after applying the operation 
        import heapq as hp
        from math import ceil
        max_heap = []
        class NODE:
            def __init__(self,val):
                self.val = val
            def __lt__(self,other):
                return self.val > other.val
        for num in nums:
            hp.heappush(max_heap,NODE(num))
        score = 0
        while k > 0:
            k -= 1
            max_elm = hp.heappop(max_heap)
            score += max_elm.val
            max_elm.val = ceil(max_elm.val / 3)
            hp.heappush(max_heap,max_elm)
        return score
