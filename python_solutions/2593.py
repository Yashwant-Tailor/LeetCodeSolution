class Solution:
    def findScore(self, nums: List[int]) -> int:
        # solution overview
        # maintain the curr minimum element (we can take help of min heap)
        # also maintain the index of elements (we can take help of hashmap)
        # also maintain the currently marked indices 
        import heapq as hp
        from collections import deque
        min_heap = []
        idx_hashmap = {}
        freq_num = {}
        vis_idx = [False for i in range(len(nums))]
        for idx,num in enumerate(nums):
            hp.heappush(min_heap,num)
            if num in idx_hashmap:
                idx_hashmap[num].append(idx)
                freq_num[num] += 1
            else:
                idx_hashmap[num] = deque()
                idx_hashmap[num].append(idx)
                freq_num[num] = 1
        score = 0
        marked_elm_count = 0
        while marked_elm_count < len(nums):
            curr_min = min_heap[0]
            # first find the minimum element which has frequency greater than 0
            while freq_num[curr_min] == 0:
                hp.heappop(min_heap)
                curr_min = min_heap[0]
            curr_min_elm_idx = idx_hashmap[curr_min][0]
            # for this minimum element find the smallest index which is not marked
            while vis_idx[curr_min_elm_idx] :
                idx_hashmap[curr_min].popleft()
                curr_min_elm_idx = idx_hashmap[curr_min][0]
            # update the score , vis_idx, and freq_num
            score += curr_min
            vis_idx[curr_min_elm_idx] = True
            marked_elm_count += 1
            freq_num[curr_min] -= 1
            # check for adjacant element in right side
            if curr_min_elm_idx + 1 < len(nums) and not vis_idx[curr_min_elm_idx+1]:
                vis_idx[curr_min_elm_idx+1] = True
                marked_elm_count += 1
                freq_num[nums[curr_min_elm_idx+1]] -= 1
            # check for adjacent element in left side
            if curr_min_elm_idx - 1 >= 0 and not vis_idx[curr_min_elm_idx-1]:
                vis_idx[curr_min_elm_idx-1] = True
                marked_elm_count += 1
                freq_num[nums[curr_min_elm_idx-1]] -= 1
        return score


        
        
