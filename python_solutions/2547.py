class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        # Solution Overview
        # simple solution (will not work with the given constraints)
        # if find all the splits of a given array (using recursion) , and for each split we calculate the cost , return the minimum cost
        # to improve this solution we can use dynamic programming to store the results of some state and in this way we can avoid doing recalculation of the same state
        # for a given subarray we can calculate the importance value 
        # now if we pre-calculate the importance value of each subarray , then use dp to calculate the optimal cost of nums array
        len_nums = len(nums)
        imp_val = [[0 for idx1 in range(len_nums+1)] for idx2 in range(len_nums+1)]
        for idx1 in range(1,len_nums+1):
            unique_elm = set()
            non_unique_elm = set()
            trimmed_val = 0
            for idx2 in range(idx1,len_nums+1):
                elm = nums[idx2-1]
                if elm in non_unique_elm:
                    trimmed_val += 1
                elif elm in unique_elm:
                    unique_elm.discard(elm)
                    non_unique_elm.add(elm)
                    trimmed_val += 2
                else:
                    unique_elm.add(elm)
                imp_val[idx1][idx2] = trimmed_val+k
                
        INF = len_nums * (k+1)
        cost = [INF for idx in range(len_nums+1)]
        cost[0] = 0
        for right_idx in range(1,len_nums+1):
            for left_idx in range(right_idx,0,-1):
                cost[right_idx] = min(cost[right_idx],cost[left_idx-1]+imp_val[left_idx][right_idx])
        return cost[len_nums]
