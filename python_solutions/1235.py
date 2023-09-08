class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        new_time = []
        for i in range(len(startTime)):
            new_time.append((startTime[i],endTime[i],profit[i]))
        new_time.sort(key = lambda x : x[1])
        prof = []
        max_p = 0
        from bisect import bisect_left
        for p in new_time:
            max_p = max(max_p,p[2])
            idx = bisect_left(prof,p[0],key=lambda x : x[0])
            if idx < len(prof) and prof[idx][0] <= p[0]:
                max_p = max(max_p , p[2] + prof[idx][1])
            if idx-1 >= 0:
                max_p = max(max_p,p[2] + prof[idx-1][1])
            if len(prof) > 0 and p[1] == prof[-1][0]:
                prof[-1] = (prof[-1][0],max_p)
            else:
                prof.append((p[1],max_p))
        return prof[-1][1]
        
