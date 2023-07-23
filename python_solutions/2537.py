class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # simple solution would be using O(n^2) algorithm to fix two indicies and then count the number pairs in between these two indices which follows the condition 
        # we can use two pointer instead to do the same calculation

        start = 0
        from collections import defaultdict
        freq = defaultdict(lambda : 0)
        ans = 0
        curr_pair_count = 0
        for idx , num in enumerate(nums):
            # whatever good subarrays we have till idx-1 will also be good subarrays if we add the index idx
            delta = (freq[num] * (freq[num]-1))//2
            freq[num] += 1
            delta = (freq[num] * (freq[num]-1))//2 - delta
            curr_pair_count += delta
            while start <= idx and curr_pair_count >= k:
                ans += (len(nums)-idx)
                start_num = nums[start]
                delta = (freq[start_num]*(freq[start_num]-1))//2
                freq[start_num] -= 1
                delta = (freq[start_num]*(freq[start_num]-1))//2 - delta
                curr_pair_count += delta
                start += 1
        return ans


