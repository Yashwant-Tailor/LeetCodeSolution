class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Solution Overview
        # sort the ballon diameters ,according to their, end
        # then burst the overlapping ballons
        points.sort(key=lambda x : x[1])
        idx = 0
        arrow_cnt = 0
        while idx < len(points):
            curr_end = points[idx][1]
            arrow_cnt += 1
            while idx < len(points) and points[idx][0] <= curr_end:
                idx += 1
        return arrow_cnt
