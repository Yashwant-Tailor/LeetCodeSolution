class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # Solution Overview
        # it is optimal reaarange the array into sorted decreasing order
        nums.sort(reverse=True)
        curr_sum = 0
        ans = 0
        for num in nums:
            curr_sum += num
            if curr_sum > 0:
                ans += 1
            else:
                return ans
        return ans
