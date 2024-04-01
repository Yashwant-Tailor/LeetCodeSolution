class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        arr_cnt = 0 
        idx = 0 
        while idx < len(nums):
            curr_num = nums[idx] 
            arr_len = 1
            idx += 1
            while idx < len(nums) and nums[idx] != curr_num :
                curr_num = nums[idx]
                arr_len += 1
                idx += 1
            arr_cnt += (arr_len * (arr_len+1))//2
        return arr_cnt
        
