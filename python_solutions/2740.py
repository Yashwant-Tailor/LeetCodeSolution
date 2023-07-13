class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        # Solution Overview
        # after sorting the nums in increasing order
        # consider the pair nums[-1] and nums[-2]
        # it is clear that either nums[-1] and nums[0:-2] will be nums1 and nums[-2] will be in nums2 (if possible)
        # if this case is not possible than consider next pair nums[-2] and nums[-3]
        # if we continue like this then we know that minimum value will be difference between the adjacent pair in sorted array (minimized partition value)
        nums.sort()
        ans = None
        for idx in range(1,len(nums)):
            diff = abs(nums[idx]-nums[idx-1])
            ans = min(ans,diff) if ans is not None else diff
        return ans
