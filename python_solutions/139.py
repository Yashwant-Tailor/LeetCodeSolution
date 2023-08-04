class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Solution Overview
        # let's calculate the answer using dynamic programming
        # dp[i] = will store true if we can break down the substring s[0:i] otherwise it will be false
        # to calculate dp[i] will check for every substring ending at index i , is included in wordDict and dp[i-length_of_the_substring] should be true

        s_len = len(s)
        can_seg = [False for itr in range(s_len+1)]
        can_seg[0] = True
        for end_idx in range(1,s_len+1):
            for start_idx in range(1,end_idx+1):
                if s[start_idx-1:end_idx] in wordDict:
                    can_seg[end_idx] |= can_seg[start_idx-1]
        return can_seg[s_len]
