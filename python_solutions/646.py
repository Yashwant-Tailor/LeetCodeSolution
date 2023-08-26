class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # solution Overview
        # if we sort the pairs , with their endpoint (i.e. right), then the longest chain can be formed by greedily picking up the elements while iterating from left to right
        pairs.sort(key = lambda x : x[1])
        long_len = 1
        curr_end = pairs[0][1]
        idx = 1
        while idx < len(pairs):
            if pairs[idx][0] > curr_end:
                long_len += 1
                curr_end = pairs[idx][1]
            idx += 1
        return long_len
