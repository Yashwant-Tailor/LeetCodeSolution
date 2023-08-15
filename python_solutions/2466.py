class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Solution Overview
        # pretty classic dynamic programming problem
        # we will use bottom-up approach to calculate the states of dp
        # dp[i] = will denote the count of substring of length 'i' 
        # for transitions
        # we can make length 'i' substring by append zero time '0' to string of length (i-zero) 
        # same thing we can do it for one ('1')

        dp = [0 for i in range(high+1)]
        dp[0] = 1 # Base case
        total_cnt = 0
        MOD = int(1e9+7)
        for str_len in range(1,high+1):
            if str_len-zero >= 0:
                dp[str_len] += dp[str_len-zero]
            if str_len-one >= 0:
                dp[str_len] += dp[str_len-one]
            dp[str_len] %= MOD
            if low <= str_len <= high:
                total_cnt += dp[str_len]
                total_cnt %= MOD
        return total_cnt


