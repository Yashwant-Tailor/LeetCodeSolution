class Solution:
    def get_one_idx(self,nums,one_loc):
        idx = 0
        while one_loc > 0:
            if nums[idx] == 1:
                one_loc -= 1
            idx += 1
        return idx-1
    def get_left_moves(self,nums,left_idx,right_idx):
        moves = 0
        curr_one = 0
        zero_cnt = 0
        for idx in range(left_idx , right_idx):
            if nums[idx] == 1:
                curr_one += 1
            else:
                moves += curr_one
                zero_cnt += 1
        return zero_cnt,moves
    def get_right_moves(self,nums,left_idx,right_idx):
        moves = 0
        curr_one = 0
        zero_cnt = 0
        for idx in range(right_idx,left_idx,-1):
            if nums[idx] == 1:
                curr_one += 1
            else:
                moves += curr_one
                zero_cnt += 1
        return zero_cnt,moves
    def minMoves(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # if we consider k consecutive ones in the array , then minimum number of moves will be equal to minimum moves to remove zeros present in between one
        # a zero can be moved either left or right side 
        # it is always optimal to move the zero in the side where we have less number of ones (as this will result in minimum moves to remove the zero)

        # so zeros in the window of k consecutive ones , either will be removed by moving in left or right side (based on the ones around these zeros)
        if k == 1:
            return 0
        mid_one = (k+1)//2
        left_cost = (k-1)//2
        right_cost = k//2
        left_idx = self.get_one_idx(nums,1)
        right_idx = self.get_one_idx(nums,k)
        mid_idx = self.get_one_idx(nums,mid_one)
        l_zero,left_moves = self.get_left_moves(nums,left_idx,mid_idx)
        r_zero,right_moves = self.get_right_moves(nums,mid_idx,right_idx)
        total_moves = left_moves + right_moves
        rem_window = sum(nums) - k
        while rem_window > 0:
            rem_window -= 1
            left_moves -= l_zero # for every left zero decrease one move
            left_idx += 1
            while nums[left_idx] != 1:
                l_zero -= 1
                left_idx += 1
            mid_idx += 1
            while nums[mid_idx] != 1:
                l_zero += 1
                left_moves += left_cost
                mid_idx += 1
                r_zero -= 1
                right_moves -= right_cost
            right_idx += 1
            while nums[right_idx] != 1:
                r_zero += 1
                right_idx += 1
            right_moves += r_zero
            total_moves = min(total_moves,left_moves+right_moves)
        return total_moves
            



            
