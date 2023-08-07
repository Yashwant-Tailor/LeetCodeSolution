class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # Solution Overview

        dp  = [[0 for j in range(n+1)] for i in range(goal+1)]
        dp[0][0] = 1
        MOD = int(1e9+7)
        for i in range(1,goal+1):
            for j in range(1,n+1):
                dp[i][j] = (dp[i-1][j-1] * (n-j+1))%MOD
                if j > k:
                    dp[i][j] += (dp[i-1][j] * (j-k))%MOD
                    dp[i][j] %= MOD
        return dp[goal][n]

