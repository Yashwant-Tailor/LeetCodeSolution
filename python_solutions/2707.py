class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Solution Overview
        # use dynamic programming to calculate the optimal break down of s
        # dp[i+1][j+1] will denote the minimum left over if we break down the s till index i (i.e. s[0:i]) using first j words in dictionary (i.e. dictionary[0:j])

        n = len(s)
        m = len(dictionary)
        dp = [[n for j in range(n+1)] for i in range(m+1)]
        # set intial state correctly
        for i in range(m+1):
            dp[i][0] = 0
        hashmap = {}
        for i , word in enumerate(dictionary):
            hashmap[word] = True
            for j in range(n):
                # in range (0,j) make all word ending at index j
                curr_word = ''
                k = j
                while k >= 0:
                    curr_word = s[k] + curr_word
                    curr_leftover = dp[i+1][k]
                    if curr_word in hashmap:
                        curr_leftover += 0
                    else:
                        curr_leftover += len(curr_word)
                    dp[i+1][j+1] = min(dp[i+1][j+1],curr_leftover)
                    k -= 1
        return dp[m][n]


