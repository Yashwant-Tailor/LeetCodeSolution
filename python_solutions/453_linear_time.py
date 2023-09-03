class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Solution Overview
        # adding 1 to (n-1) elements is same as subtracting 1 from single element
        # final answer would be sum(nums) - n * min(nums)
        return sum(nums) - len(nums) * min(nums)
        
