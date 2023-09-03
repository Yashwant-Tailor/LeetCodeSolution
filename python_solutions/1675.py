class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Solution Overview
        # if we make every element even by applying the operation, then optimally divide the maximum number by two if we can and check if we can decrease the deviation
        import heapq as hp
        max_heap = []
        min_num = int(1e11)
        for num in nums:
            new_num = num
            if num%2 == 1:
                new_num *= 2
            min_num = min(min_num,new_num)
            hp.heappush(max_heap,-1 * new_num)
        max_num = -1 * max_heap[0]
        dev = max_num-min_num
        while True:
            curr_max = -1 * hp.heappop(max_heap)
            if curr_max%2 == 1:
                break
            curr_max >>= 1
            min_num = min(min_num,curr_max)
            hp.heappush(max_heap, -1 * curr_max)
            curr_max = -1 * max_heap[0]
            curr_dev = curr_max - min_num
            dev = min(dev,curr_dev)
        return dev
        
        
        
