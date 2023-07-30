class Solution:
    def isPos(self,nums,max_val):
        extra_add = 0
        for i in range(len(nums)-1,-1,-1):
            num = nums[i] + extra_add
            if i == 0:
                return num <= max_val
            else:
                if num <= max_val:
                    extra_add = 0
                else:
                    extra_add = num - max_val
        
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # Solution Overview
        # binary search for the optimal maximum value and check that this maximum is achievable or not (it can be done in O(N) time)

        max_st = 0
        max_en = sum(nums)+1
        while max_st < max_en:
            max_mid = max_st + (max_en - max_st)//2
            if self.isPos(nums,max_mid):
                max_en = max_mid
            else:
                max_st = max_mid + 1
        return max_en

        
                
