class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Solution Overview
        # sort the start point then use binary serach to find the optimal start
        start = []
        for idx, interval in enumerate(intervals):
            start.append((idx,interval[0]))
        start.sort(key= lambda x : x[1])
        from bisect import bisect_left
        ans = []
        for interval in intervals:
            curr_end = interval[1]
            idx = bisect_left(start,curr_end,key=lambda x : x[1])
            if idx == len(start):
                ans.append(-1)
            else:
                ans.append(start[idx][0])
        return ans
