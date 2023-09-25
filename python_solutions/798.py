class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        # Solution Overview
        # for every number there is a range of rotations which will lead to have one point from the given number 
        # try to find the range and then update that range using prefix sum
        points = [0 for rot in range(len(nums)+1)]
        for idx,num in enumerate(nums):
            if idx >= num:
                points[0] += 1
                points[idx-num+1] -= 1
                points[idx+1] += 1
                points[len(nums)] += -1
            else:
                points[idx+1] += 1
                points[len(nums)-num+idx+1] -= 1
        su = 0
        idx = 0
        ma = 0
        ma_idx = -1
        while idx < len(points):
            su += points[idx]
            points[idx] = su
            if points[idx] > ma:
                ma = points[idx]
                ma_idx = idx
            idx += 1
        return ma_idx
        
