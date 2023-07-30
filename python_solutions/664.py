class Solution:
    def strangePrinter(self, s: str) -> int:
        # Solution Overview
        # use dynamic programming to calculate the optimal number of turns 
        # dp[i][j] = will store the number of turns required to print the string s[i:j] (both index included)
        # we will first calculate the answer for all substring of length 1 (BASE CASE)
        # then iteratively calculate the answer for substring of length > 1 till substring of length == n (length of s)
        n = len(s)
        dp = [[n for j in range(n+1)] for i in range(n+1)]
        dp[0][0] = 0
        for j in range(1,n+1):
            dp[j][j] = 1
        for i in range(1,n):
            j = 1
            while j+i<= n:
                k = j
                while k < j+i:
                    dp[j][j+i] = min(dp[j][j+i],dp[j][k] + dp[k+1][j+i])
                    k += 1
                if s[j-1] == s[j+i-1] or s[j+i-2] == s[j+i-1]:
                    dp[j][j+i] = min(dp[j][j+i],dp[j][j+i-1])
                j += 1
        return dp[1][n]
