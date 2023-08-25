class Solution:
    def minInsertions(self, s: str) -> int:
        # Solution Oveview
        # we can calculate the answer using DP
        # dp[i][j] = will be minimum number of insert operations to make , substring s[i:j+1] palindromic

        len_s = len(s)
        min_ins = [[len_s for idx1 in range(len_s+1)] for idx2 in range(len_s+1)]
        for i in range(1,len_s+1):
            min_ins[i][i] = 0
            if i > 1:
                if s[i-2] == s[i-1]:
                    min_ins[i-1][i] = 0
                else:
                    min_ins[i-1][i] = 1
        for sub_str_len in range(2,len_s+1):
            left_idx = 0
            while left_idx + sub_str_len <= len_s:
                right_idx = left_idx + sub_str_len
                min_ins[left_idx][right_idx] = min(min_ins[left_idx][right_idx-1],min_ins[left_idx+1][right_idx]) + 1
                if s[left_idx-1] == s[right_idx-1]:
                    min_ins[left_idx][right_idx] = min(min_ins[left_idx][right_idx],min_ins[left_idx+1][right_idx-1])
                left_idx += 1
        return min_ins[1][len_s]
