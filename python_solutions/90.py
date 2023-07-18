class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Solution Overview
        # iterate over all possible subsests and keep track of unique subsets using hashmap

        ans = set()
        n = len(nums)
        for i in range(0 , 2 ** n):
            curr_subset = []
            for j in range(n):
                if i & (1<<j):
                    curr_subset.append(nums[j])
            curr_subset.sort()
            ans.add(tuple(curr_subset))
        return list(ans)
