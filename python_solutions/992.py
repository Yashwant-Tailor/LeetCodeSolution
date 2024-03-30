class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        l , r1 , r2 = 0 , 0 , 0
        map1 = {}
        arr_cnt = 0
        while l < len(nums):
            while r1 < len(nums) and len(map1) < k:
                if nums[r1] in map1:
                    map1[nums[r1]] += 1
                else:
                    map1[nums[r1]] = 1
                if r1 == r2:
                    r2 += 1
                r1 += 1
            while r2 < len(nums) and nums[r2] in map1:
                r2 += 1
            if len(map1) == k:
                arr_cnt += r2-r1+1
            map1[nums[l]] -= 1
            if map1[nums[l]] == 0:
                map1.pop(nums[l])
            l += 1
            
        return arr_cnt
