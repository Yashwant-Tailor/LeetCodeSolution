class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        # Solution Overview
        # if we calculate the answer for all the number in decreasing order than its clear that for a number the maximum length increasing sequence would be the number which is greater than this number and it is in the same row or column as this number
        # for each row and column we can maintain the maximum increasing sequence length and then we can iteratively update it
        num_arr = []
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            for j in range(n):
                num_arr.append([mat[i][j],(i,j)])
        num_arr.sort(key=lambda x : x[0])
        row_max = [0 for i in range(m)]
        col_max = [0 for j in range(n)]
        longest_inc_len = 0
        while len(num_arr) > 0:
            curr_val = num_arr[-1][0]
            eq_num_loc = []
            # for each point having equal value calculate the length first
            while len(num_arr) > 0 and curr_val == num_arr[-1][0]:
                curr_num = num_arr.pop()
                row , col = curr_num[1]
                curr_inc_len = max(row_max[row],col_max[col]) + 1
                longest_inc_len = max(longest_inc_len,curr_inc_len)
                eq_num_loc.append([curr_num[1],curr_inc_len])
            # then update the longest inc_len for each row and column 
            for num_loc , inc_len in eq_num_loc:
                row,col = num_loc
                row_max[row] = max(row_max[row],inc_len)
                col_max[col] = max(col_max[col],inc_len)
        return longest_inc_len

