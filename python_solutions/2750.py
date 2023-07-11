class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        # Solution overview
        # use dynamic programming to store the result of current good subarrys till ith 1
        # zeros between two 1's will increase the count

        curr_idx = 0
        curr_ans = 1
        MOD = int(1e9 + 7)
        while curr_idx < len(nums) and nums[curr_idx] == 0:
            curr_idx += 1
        if curr_idx == len(nums):
            return 0
        while curr_idx < len(nums):
            # calculate the length of pattern 000000...001
            pattern_len = 0
            while curr_idx < len(nums) and nums[curr_idx] == 0:
                pattern_len += 1
                curr_idx += 1
            if curr_idx == len(nums):
                # we have the pattern 00000.0000
                # we dont have 1 in the end
                continue
            # this statement will always be true
            if nums[curr_idx] == 1:
                pattern_len += 1
                curr_idx += 1
            curr_ans = (curr_ans * pattern_len)%(MOD)
        return curr_ans
