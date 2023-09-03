class Solution:
    def get_max_coin(self,left,right,nums,coin):
        if coin[(left,right)] != -1:
            return coin[(left,right)]
        left_num = 1
        right_num = 1
        if 0 <= left < len(nums):
            left_num = nums[left]
        if 0 <= right < len(nums):
            right_num = nums[right]
        max_coin = 0
        for idx in range(left+1,right):
            curr_coin = left_num * nums[idx] * right_num
            max_coin  = max(max_coin, curr_coin + self.get_max_coin(left,idx,nums,coin)+self.get_max_coin(idx,right,nums,coin))
        coin[(left,right)] = max_coin
        return max_coin
    def maxCoins(self, nums: List[int]) -> int:
        # Solution Overview
        # refer to this link
        # https://leetcode.com/problems/burst-balloons/solutions/892552/for-those-who-are-not-able-to-understand-any-solution-with-diagram/
        from collections import defaultdict
        coin = defaultdict(lambda : -1)
        return self.get_max_coin(-1,len(nums),nums,coin)

        
