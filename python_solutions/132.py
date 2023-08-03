class Solution:
    def minCut(self, s: str) -> int:
        # Solution Overview
        # let say dp[i] = val 
        # where dp[i] will store the minimum cut needed to make the partition of s[0:i] such that every partition is palindrome
        # now to calculate dp[i+1] we will find every palindrome substring of s[0:i+1] which ends on index i+1 and we will update dp[i+1] = min(dp[i+1],dp[i+1-(length of current substring in consideration)] + 1)

        # to check that current substring is palindrom or not we can pre-calculate another palindrom dp
        # let say pal_dp[i][j] = True , if s[i:j] is palindrome
        # other wise dp[i][j] = False
        # now to calculate dp[i][j] , we can check that if (s[i] == s[j]) and (dp[i+1][j-1] == True)

        n = len(s)
        pal_dp = [[False for j in range(n+1)] for i in range(n+1)]
        for i in range(n+1):
            pal_dp[i][i] = True # Base case , as every string of length one is palindrome
        for sub_len in range(1,n+1):
            start_idx = 1
            while start_idx + sub_len < n+1:
                end_idx = start_idx+sub_len
                if s[start_idx-1] == s[end_idx-1]:
                    if sub_len > 2:
                        pal_dp[start_idx][end_idx] = pal_dp[start_idx+1][end_idx-1]
                    else:
                        pal_dp[start_idx][end_idx] = True
                start_idx += 1
        MAX_CUT = n-1
        cut_dp = [MAX_CUT for i in range(n+1)]
        cut_dp[0] = -1
        for end_idx in range(1,n+1):
            for start_idx in range(1,end_idx+1):
                if pal_dp[start_idx][end_idx]:
                    cut_dp[end_idx] = min(cut_dp[end_idx],cut_dp[start_idx-1]+1)
        return cut_dp[n]
