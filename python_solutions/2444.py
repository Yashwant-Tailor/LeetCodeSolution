class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        arr_cnt = 0
        ls_min, ls_max,ls_out = 0 , 0 , 0
        for idx,num in enumerate(nums):
            idx += 1
            if num == minK:
                ls_min = idx
            if num == maxK :
                ls_max = idx
            if num < minK or num > maxK:
                ls_out = idx
            arr_cnt += max(0 , min(ls_min ,ls_max) - ls_out)
        return arr_cnt
