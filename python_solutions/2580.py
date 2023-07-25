class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # Solution Overview
        # if there is no overlapping range then answer for n range would be 2^n
        # we just need to merge the overlapping ranges to find the correct value of n

        ranges.sort(key= lambda x : x[0])
        idx = 0 
        non_overlapping_range_count = 0
        while idx < len(ranges):
            curr_end = ranges[idx][1]
            idx += 1
            while idx < len(ranges) and curr_end >= ranges[idx][0]:
                curr_end = max(curr_end,ranges[idx][1])
                idx += 1
            non_overlapping_range_count += 1
        ans = 1
        curr_2p = 2
        MOD = int(1e9+7)
        while non_overlapping_range_count > 0:
            if non_overlapping_range_count & 1:
                ans *= curr_2p
                ans %= MOD
            non_overlapping_range_count >>= 1
            curr_2p *= curr_2p
            curr_2p %= MOD
        return ans

