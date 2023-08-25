class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Solution Overview
        # it is clear that weights[0] and wieghts[n-1] will always be int score
        # now if we take make group then we need to take two adjacent element from the array and it will create two group for us
        # to find the maximum we will take sum of adjacent pairs which will result in maximum sum , for minimum we will do the same to get the minimum result
        len_w = len(weights)
        min_score = weights[0] + weights[len_w-1]
        max_score = weights[0] + weights[len_w-1]

        pair_sum = []
        for i in range(len_w-1):
            pair_sum.append(weights[i] + weights[i+1])
        pair_sum.sort()
        # we need to take (k-1) pairs to make (k) groups
        idx = 0
        while idx < (k-1):
            max_score += pair_sum[len(pair_sum)-1-idx]
            min_score += pair_sum[idx]
            idx += 1
        return max_score-min_score
