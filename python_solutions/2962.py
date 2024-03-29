class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        max_loc = []
        max_loc.append(-1)
        for idx,num in enumerate(nums):
            if num == max_val:
                max_loc.append(idx)
        max_loc.append(len(nums))
        arr_cnt = 0
        for idx in range(1,len(nums)+1):
            if idx + k-1 < len(max_loc):
                arr_cnt += (max_loc[idx]-max_loc[idx-1]) * (len(nums)-max_loc[idx+k-1])
        return arr_cnt
        
