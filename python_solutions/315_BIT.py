class Solution:
    class BIT:
        def __init__(self,n):
            self.range_nums = n
            self.bit = [0 for idx in range(n)]
        def get_sum(self,r,l):
            return self.pref_sum(r) - self.pref_sum(l-1)
        def pref_sum(self,idx):
            res = 0
            while idx >= 0:
                res += self.bit[idx]
                idx = (idx & (idx+1)) - 1
            return res
        def update_val(self,idx,val):
            while idx < self.range_nums:
                self.bit[idx] += val
                idx = (idx | (idx+1))
    def countSmaller(self, nums: List[int]) -> List[int]:
        # solution Overview
        # we can use binary indexed tree (BIT or FENWICH TREE) 
        # scan the array in reverse orde then update the BIT accordingly
        mi = min(nums)
        ma = max(nums)
        if mi > 0:
            mi = 0
        bit = self.BIT(ma-mi+1)
        ans = [0 for idx in range(len(nums))]
        for idx in range(len(nums)-1,-1,-1):
            ans[idx] = bit.get_sum(nums[idx]-mi-1,0)
            bit.update_val(nums[idx]-mi,1)
        return ans



        
