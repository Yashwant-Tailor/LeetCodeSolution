class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Solution Overview
        points.sort(key=lambda x : x[1])
        import heapq as hp
        min_heap = []
        for idx,point in enumerate(points):
            st,en = point
            hp.heappush(min_heap,(st,idx))
        is_burst = [False for idx in range(len(points))]
        idx = 0
        arrow_cnt = 0
        while idx < len(points):
            if not is_burst[idx]:
                curr_end = points[idx][1]
                while len(min_heap)>0 and min_heap[0][0] <= curr_end:
                    st,n_idx = hp.heappop(min_heap)
                    is_burst[n_idx] = True
                arrow_cnt += 1
            idx += 1
        return arrow_cnt
