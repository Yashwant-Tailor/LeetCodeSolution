class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        # Solution overview
        # simple implement as mentioned

        ans = []
        curr_max = -1
        curr_score = 0
        for num in nums:
            curr_max = max(curr_max,num)
            curr_score += num + curr_max
            ans.append(curr_score)
        return ans
