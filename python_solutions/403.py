class Solution:
    def get_next_loc(self,curr_loc,jump_len,idx_map):
        loc1 = curr_loc + (jump_len-1)
        loc2 = curr_loc + (jump_len)
        loc3 = curr_loc + (jump_len+1)
        res = []
        if loc1 > curr_loc and loc1 in idx_map:
            res.append((loc1,jump_len-1))
        if loc2 > curr_loc and loc2 in idx_map:
            res.append((loc2,jump_len))
        if loc3 > curr_loc and loc3 in idx_map:
            res.append((loc3,jump_len+1))
        return res
    def canCross(self, stones: List[int]) -> bool:
        # Solution Overview
        # it's clear that we need to use the dynamic programming to store the states of frog last jump, so that we can upda the other states
        # DP[i] = will store the units of last jump in which frog will land on the stones[i]
        # from the given constrants , it is clear that we will have at O(n*n) space complexity
        len_stones = len(stones)
        prev_jump_len = [set() for idx in range(len_stones)]
        idx_map = {}
        for idx,stone_loc in enumerate(stones):
            idx_map[stone_loc] = idx
        # BASECASE (given in the problem)
        prev_jump_len[0].add(0)
        # as we want to jump on the last stones , so we don't need to iterate for that stone
        for idx in range(0,len_stones-1):
            for jump_len in prev_jump_len[idx]:
                for next_stone_loc,next_jump_len in self.get_next_loc(stones[idx],jump_len,idx_map):
                    next_idx = idx_map[next_stone_loc]
                    prev_jump_len[next_idx].add(next_jump_len)
        return True if len(prev_jump_len[len_stones-1]) > 0 else False

