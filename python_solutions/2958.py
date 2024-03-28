class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(lambda : 0)
        max_len = 0
        left = 0
        for idx,num in enumerate(nums):
            while freq[num] >= k:
                freq[nums[left]] -= 1
                left += 1
            freq[num] += 1
            max_len = max(max_len ,idx-left+1 )
        return max_len
