class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # Solution Overview
        # count of each fruit in should be same in each basket
        # first calculate the difference between count of a fruit type in both basket
        # the total count of such differences will be same in basket1 and basket2 (let say we have n such frutis which needs to be moved from basket1 to basket2 , then we will also have n such fruits in basket2 which will be moved to basket1) , total_count = 2*n
        # now out of these 2*n fruits we need to take the first n minimum numbers
        # or we take help of minimum element , we start swap two indices with the help of this minimum number
        from collections import defaultdict
        elm_cnt = defaultdict(lambda : 0)
        min_elm = int(1e9)+1
        for idx in range(len(basket1)):
            elm_cnt[basket1[idx]] += 1
            elm_cnt[basket2[idx]] -= 1
            min_elm = min(min_elm,min(basket1[idx],basket2[idx]))
        diff_elm = []
        for cost,cnt in elm_cnt.items():
            if cnt < 0:
                cnt *= -1
            if cnt%2 == 1:
                return -1
            cnt //= 2
            diff_elm += [cost for idx in range(cnt)]
        diff_elm.sort()
        n = len(diff_elm)//2
        total_cost = 0
        for i in range(n):
            total_cost += min(diff_elm[i],2*min_elm)
        return total_cost
