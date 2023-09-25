class Solution:
    def num_ways(self,curr_sum,nums,ways):
        if ways[curr_sum] != -1:
            return ways[curr_sum]
        if curr_sum == 0:
            ways[curr_sum] = 1
            return 1
        ways[curr_sum] = 0
        for num in nums:
            if curr_sum - num >= 0:
                ways[curr_sum] += self.num_ways(curr_sum-num,nums,ways)
        return ways[curr_sum]
    def combinationSum4(self, nums: List[int], target: int) -> int:
        ways = [-1 for i in range(target+1)]
        return self.num_ways(target,nums,ways)
