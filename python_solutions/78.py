class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Solution Overview
        # do recursion

        n = len(nums)
        ans = []
        for i in range(0 , 2 ** n):
            subset = []
            for j in range(n):
                if i & (1<<j):
                    subset.append(nums[j])
            ans.append(subset)
        return ans
