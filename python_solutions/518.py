class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Solution Overview
        # use dynamic programming to store the state
        n = len(coins)
        dp = [[0 for j in range(n+1)] for i in range(amount+1)]
        for j in range(n+1):
            dp[0][j] = 1
        for i in range(1,amount+1):
            for j in range(1 , n+1):
                dp[i][j] = dp[i][j-1]
                curr_val = coins[j-1]
                while i >= curr_val:
                    dp[i][j] += dp[i-curr_val][j-1]
                    curr_val += coins[j-1]
        return dp[amount][n]
