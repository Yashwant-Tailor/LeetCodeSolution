class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # Solution Overview
        # use dynamic programming to store the result
        # min_cut[i] = val , will store the minimum cut required to s[0:i] 
        # to calculate min_cut[i] , we can take help all substring ending at index i and has value less than k

        s_len = len(s)
        INF_CUT = s_len+1
        min_cut = [INF_CUT for i in range(s_len+1)]
        min_cut[0] = 0
        for end_idx in range(1,s_len+1):
            start_idx = end_idx
            while start_idx >= 1 and int(s[start_idx-1:end_idx])<=k:
                min_cut[end_idx] = min(min_cut[end_idx],min_cut[start_idx-1]+1)
                start_idx -= 1
        return -1 if min_cut[s_len] == INF_CUT else min_cut[s_len]
