class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        # Solution Overview
        # if we keep track of all the indices where we have equal number , then the answer is only possible for out of all unique number for which we have equal number in , we should have at least these many indices in where none of the nums1 or nums2 is equal to the number , if this is not the case then the answer is not possible
        from collections import defaultdict,deque
        eq_idx_cnt = defaultdict(lambda : 0)
        idx_grp = set()
        total_eq_cnt = 0
        single_max_eq_cnt = 0
        single_max_eq_num = None
        for idx in range(len(nums1)):
            if nums1[idx] == nums2[idx]:
                idx_grp.add(idx)
                total_eq_cnt += 1
                eq_idx_cnt[nums1[idx]] += 1
                if eq_idx_cnt[nums1[idx]] > single_max_eq_cnt:
                    single_max_eq_cnt = eq_idx_cnt[nums1[idx]]
                    single_max_eq_num = nums1[idx]
        # please refer to this link to get more insights about the solution 
        # https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/solutions/2898175/pigeonhole-with-o-n-algorithm/
        if single_max_eq_cnt > total_eq_cnt//2:
            idx = 0
            while idx < len(nums1) and single_max_eq_cnt > total_eq_cnt//2:
                if (nums2[idx] != nums1[idx]) and nums2[idx] != single_max_eq_num and nums1[idx] != single_max_eq_num:
                    total_eq_cnt += 1
                    idx_grp.add(idx)
                idx += 1
            if single_max_eq_cnt > total_eq_cnt//2:
                return -1
        total_cost = 0
        for idx in idx_grp:
            total_cost += idx
        return total_cost
                
