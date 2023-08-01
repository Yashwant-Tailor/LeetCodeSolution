class Solution:
    def dfs_update_streak_len(self,num,ind_hashmap,vis,longest_square_streak_len):
        vis[num] = True
        curr_len = 1
        sq_num = num * num
        if sq_num in ind_hashmap:
            if vis[sq_num]:
                curr_len += longest_square_streak_len[sq_num]
            else:
                curr_len += self.dfs_update_streak_len(sq_num,ind_hashmap,vis,longest_square_streak_len)
        longest_square_streak_len[num] = curr_len
        return curr_len
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Solution Overview
        # let's say we have first number in the subsequence , then adding the further element would require us to find the square of the current element in the array and if it is present then we can add the next element and repeat the same process again
        # this suggest that if we can mantain indices hashmap , and perform the dfs traversal starting from the current index and moving onto the next index with the help of indices hashmap will finally give us the length of the longest square streak

        ind_hashmap = {}
        vis = {}
        longest_square_streak_len = {}
        for idx,num in enumerate(nums):
            if num not in ind_hashmap:
                ind_hashmap[num] = idx
                vis[num] = False
                longest_square_streak_len[num] = 0
        ans = -1
        for num in nums:
            if not vis[num]:
                curr_len = self.dfs_update_streak_len(num,ind_hashmap,vis,longest_square_streak_len)
                if curr_len > 1:
                    ans = max(ans,curr_len)
        return ans
