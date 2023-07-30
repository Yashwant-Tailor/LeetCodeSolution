class Solution:
    def isPos(self,nums,p,diff):
        pairs_count = 0
        idx = 1
        while idx < len(nums):
            if abs(nums[idx]-nums[idx-1]) <= diff:
                pairs_count += 1
                idx += 2
            else:
                idx += 1
        return pairs_count >= p
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Solution Overview
        # let's say if we fix the minimum maximum difference then we can check that this value is possible or not in O(N) time
        # just binary search to find the optimal value of minimum maximum difference
        nums.sort()
        min_diff = 0
        max_diff = int(1e9+1)

        while min_diff < max_diff:
            mid_diff = min_diff + (max_diff-min_diff)//2
            if self.isPos(nums,p,mid_diff):
                max_diff = mid_diff
            else:
                min_diff = mid_diff+1
        return max_diff
