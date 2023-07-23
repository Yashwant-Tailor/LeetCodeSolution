class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Solutin Overview
        # sort the array and use two pointer technique to find the number of fair pairs
        # first calculate the number of pairs (i,j) such that lower <= nums[i] + nums[j] {ans1}
        # then calculate the number of pairs (i,j) such that nums[i] + nums[j] <= upper {ans2}
        # final answer would be total_number_of_pairs - ans1 - ans2

        nums.sort()
        l_idx = 0
        r_idx = len(nums)-1
        lower_pair_ans = 0
        upper_pair_ans = 0
        while l_idx < r_idx:
            while r_idx > l_idx and (nums[r_idx] + nums[l_idx]) > upper:
                r_idx -= 1
            upper_pair_ans += (r_idx - l_idx)
            l_idx += 1
        l_idx = 0
        r_idx = len(nums)-1
        while l_idx < len(nums):
            while r_idx > l_idx and (nums[r_idx] + nums[l_idx]) >= lower:
                r_idx -= 1
            max_idx = max(r_idx,l_idx)
            lower_pair_ans += (len(nums)-1-max_idx)
            l_idx += 1
        ans = (len(nums) * (len(nums)-1))//2
        ans = lower_pair_ans + upper_pair_ans - ans
        return ans
