class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        # Solution Overview
        # if we replace each character in s with its value than this problem would be converted in finding the maximum sum subarray (which can be solved using kadane's algorithm)
        curr_sum = 0
        max_sum = 0
        alpha_val = {}
        for idx,char in enumerate(chars):
            alpha_val[char] = vals[idx]
        for i in range(26):
            char = chr(i + ord('a'))
            if char not in alpha_val:
                alpha_val[char] = i+1
        for char in s:
            curr_sum += alpha_val[char]
            max_sum = max(max_sum,curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
