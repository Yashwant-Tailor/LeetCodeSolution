class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Solution Overview
        # Use dynamic programming to store the some states 
        # DP[i][j] = lowest ASCII sum of deleted characters to make s1[0:i] and s2[0:j] equal.
        # This DP is similar to edit distance problem

        dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        for i in range(len(s1)):
            dp[i+1][0] = dp[i][0] + ord(s1[i])
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                dp[i][j] = min( dp[i-1][j] + ord(s1[i-1]) , dp[i][j-1] + ord(s2[j-1]) )
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1])
        return dp[len(s1)][len(s2)]
