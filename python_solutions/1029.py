class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Solution Overview
        # use dynamic programming to store the state
        # dp[i][j] will denote the minimum cost to fly every person in (1 , 2 , ... i) out of these i people j will fly to city 'a' and i-j will fly to city 'b'

        prev_dp = [0]
        n2 = len(costs)
        aCost , bCost = 0 , 1
        for i in range(1 , n2+1):
            curr_dp = [0]
            # all persons flying to city 'b'
            curr_dp[0] = prev_dp[0] + costs[i-1][bCost]
            for j in range(1 , i+1):
                # j person fly to city 'a'
                # if ith person flies to city 'a' then till (i-1)th persons 
                # we need to have j-1 people flying to city 'a'
                curr_cost = costs[i-1][aCost] + prev_dp[j-1]
                # if ith peson flies to city 'a' then till (i-1)th persons
                # we need to have j perople flying to city 'a'
                if j  == i :
                    # all persons are flying to city 'a'
                    pass
                else:
                    curr_cost = min(curr_cost ,costs[i-1][bCost] + prev_dp[j])
                curr_dp.append(curr_cost)
            # print(costs[i-1] ,curr_dp, prev_dp)
            prev_dp = curr_dp
        return prev_dp[n2//2]
