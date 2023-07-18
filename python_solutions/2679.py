class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        # Solution Overview
        # sort each row and then calculate the score at each step

        for num in nums:
            num.sort()
        ans = 0
        row_len = len(nums)
        col_len = len(nums[0])
        for j in range(col_len):
            curr_step_max = -1
            for i in range(row_len):
                curr_step_max = max(curr_step_max,nums[i][j])
            ans += curr_step_max
        return ans
