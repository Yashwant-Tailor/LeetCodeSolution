class Solution:
    def isPossible(self,capability,nums,k):
        c_robbed_house = 0
        idx = 0
        prev_idx = None
        while k > 0:
            while idx < len(nums) and nums[idx] > capability:
                idx += 1
            if idx == len(nums):
                break
            if idx-1 == prev_idx:
                idx += 1
            else:
                prev_idx = idx
                c_robbed_house += 1
                idx += 1
        return c_robbed_house >= k
    def minCapability(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # use binary serach to find the optimal value
        # while doing the binary search if we have one possible capability , we can verify that this capability is possible or not , in O(N) time
        start = min(nums)
        end = max(nums)
        while start < end:
            mid = start + (end-start)//2
            if self.isPossible(mid,nums,k):
                end = mid
            else:
                start = mid+1
        return end
