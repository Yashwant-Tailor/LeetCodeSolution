class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l , r = 0 , 0
        prod = 1
        arr_cnt = 0 
        while l < len(nums):
            if r < l:
                r = l
                prod = 1
            while r < len(nums) and prod * nums[r] < k:
                prod *= nums[r]
                r += 1
            arr_cnt += r - l
            prod //= nums[l]
            l += 1
        return arr_cnt
