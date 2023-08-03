class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # Solution Overview
        # simple 0-1 knapsack problem
        # intuation for 0-1 knapsack
        # in 0-1 knapsack we have given a max weight limit W 
        # and n items , where each item has some weight(wi) and value (vi)
        # we need to find the maximum value we can get by picking some items, while total weight of picked items will be less than or equal to W 
        # in this problem weight is actually the number of walls we can finish by picking a wall for painter1 
        # i.e. if we pick wall i to be painted by painter1 then we can finish time[i]+1 wall in the same cost[i]
        # here we need to minimize the total value of picked items 
        time_su = sum(time)
        INF = int(1e9)
        n = len(cost)
        dp = [[INF for j in range(n+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = dp[i-1][j]
                if j-time[i-1]-1>=0:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-time[i-1]-1]+cost[i-1])
                else:
                    dp[i][j] = min(dp[i][j],dp[i-1][0]+cost[i-1])
        return dp[n][n]

