class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # Solution Overview
        # as 1 <= nums[i] <= 10^9
        # now let's focus on the 2's power which are present in array
        # if we have [2^0 , 2^1 , ...., 2^i] then we can create any number (i+1) bit
        # but we can't create 2^(i+1)
        # so our answer would be the first 2's power which is not present in the array
        curr_2p = 1
        # this for loop will have atmost 32 iteration
        # as 1 <= nums[i] <= 10^9
        while curr_2p in nums:
            curr_2p <<= 1
        return curr_2p

