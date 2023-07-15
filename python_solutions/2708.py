class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # Solution Overview
        # use recursion to iterate over every possible group and calculate the strength

        n = len(nums)
        ans = nums[0]
        for i in range(1 , 2 ** n):
            # the set bits in binary representation of i will denote our selected students
            curr_strength = 1
            for j in range(13):
                if i & (1 << j):
                    curr_strength *= nums[j]
            ans = max(ans,curr_strength)
        return ans
