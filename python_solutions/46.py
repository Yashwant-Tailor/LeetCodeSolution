class Solution:
    def get_all_perm(self,nums,vis,res,curr_perm,n):
        if len(curr_perm) == n:
            res.append(curr_perm.copy())
            return
        for i in range(n):
            if not vis[i]:
                vis[i] = True
                curr_perm.append(nums[i])
                self.get_all_perm(nums,vis,res,curr_perm,n)
                curr_perm.pop()
                vis[i] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Solution Overview
        # use backtracking to find all the permutations
        res = []
        vis = [False for i in range(len(nums))]
        curr_perm = []
        self.get_all_perm(nums,vis,res,curr_perm,len(nums))
        return res
