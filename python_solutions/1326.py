class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Solution Overview
        # idea is similar to DP
        # DP[i] = will store the minimum taps we need to water the garden till end point i (start point is 0)
        # for more details refer this solution 
        # https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/editorial/
        INF = 10*n
        min_tap = [INF for idx in range(n+1)]
        for idx,rg in enumerate(ranges):
            left_idx = idx - rg
            right_idx = idx + rg
            curr_min_taps = INF
            if left_idx <= 0:
                left_idx = 0
                curr_min_taps = 1
            else:
                curr_min_taps = min_tap[left_idx] + 1
            for garden_idx in range(left_idx,min(n+1,right_idx+1)):
                min_tap[garden_idx] = min(min_tap[garden_idx],curr_min_taps)
        return -1 if min_tap[n] == INF else min_tap[n]

