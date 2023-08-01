class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # Solution Overview
        # if we can find non overlapping paths from stones[0] to stones[-1] then we can simple traverse the path
        # the minimum cost would be maximum of these two paths
        # it is optimal to choose the two consecutive stones in tha stones array into different paths 
        min_cost1 = 0
        min_cost2 = 0
        idx = 0
        loc1 = stones[idx]
        loc2 = stones[idx]
        idx = 1
        while idx < len(stones)-1:
            min_cost1 = max(min_cost1,stones[idx]-loc1)
            loc1 = stones[idx]
            idx += 2
        idx = 2
        while idx < len(stones)-1:
            min_cost2 = max(min_cost2,stones[idx]-loc2)
            loc2 = stones[idx]
            idx += 2
        min_cost1 = max(min_cost1 , stones[len(stones)-1]-loc1)
        min_cost2 = max(min_cost2, stones[len(stones)-1] - loc2)
        return max(min_cost1,min_cost2)

