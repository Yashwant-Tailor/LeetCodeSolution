class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        num_ways = [0 for j in range(target+1)]
        num_ways[0] = 1
        for curr_target in range(1,target+1):
            for num in nums:
                if curr_target - num >= 0:
                    num_ways[curr_target] += num_ways[curr_target-num]
        return num_ways[target]
