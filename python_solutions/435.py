class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Solution Overview
        # optimal strategy to sort the intervals by thier end point , then remove the overlapping intervals
        intervals.sort(key = lambda x : x[1])
        rm_cnt = 0
        idx = 0
        while idx < len(intervals):
            curr_end = intervals[idx][1]
            idx += 1
            while idx < len(intervals) and intervals[idx][0] < curr_end:
                rm_cnt += 1
                idx += 1
        return rm_cnt
        
