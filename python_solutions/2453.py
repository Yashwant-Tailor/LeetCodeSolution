class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # Solution Overview
        # if we take modulo with space the numbers with same module can be destroyed with a single feed
        # we need to return the maximum length subsequence having same modulo
        from collections import defaultdict
        mod_cnt = defaultdict(lambda : 0)
        INF = int(1e9+1)
        min_num = defaultdict(lambda : INF)
        max_cnt = 0
        max_cnt_mod = None
        for num in nums:
            mod = num%space
            mod_cnt[mod] += 1
            min_num[mod] = min(min_num[mod],num)
            if max_cnt < mod_cnt[mod]:
                max_cnt = mod_cnt[mod]
                max_cnt_mod = mod
            elif max_cnt == mod_cnt[mod] and min_num[mod] < min_num[max_cnt_mod]:
                max_cnt_mod = mod
        return min_num[max_cnt_mod]
