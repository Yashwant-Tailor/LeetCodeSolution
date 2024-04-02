import heapq as hp
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hp.heapify(nums)
        op_cnt = 0
        while len(nums)>1 and nums[0] < k:
            x  = hp.heappop(nums)
            y = hp.heappop(nums)
            hp.heappush(nums, min(x,y)*2 + max(x,y))
            op_cnt += 1
        return op_cnt
        
