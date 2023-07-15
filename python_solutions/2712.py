class Solution:
    def get_cost(self,s):
        dp_cost = []
        dp_cost.append([0,0])
        prev_char = None
        for idx,char in enumerate(s):
            cost0 = 0
            cost1 = 0
            if char == '0':
                cost0 = dp_cost[idx][0]
                if idx > 0 :
                    if s[idx-1] == '0':
                        cost1 = dp_cost[idx][1] + 1
                    else:
                        cost1 = dp_cost[idx][0] + idx + 1
                else:
                    cost1 = 1
            else:
                cost1 = dp_cost[idx][1]
                if idx > 0:
                    if s[idx-1] == '1':
                        cost0 = dp_cost[idx][0] + 1
                    else:
                        cost0 = dp_cost[idx][1] + idx + 1
                else:
                    cost0 = 1
            dp_cost.append([cost0,cost1])
        dp_cost.append([0,0])
        return dp_cost
    def minimumCost(self, s: str) -> int:
        # Solution Overview
        # calculate the minimum cost to convert the string into 
        # either 0000..000
        # or 1111.....1111
        
        left_convert_cost = self.get_cost(s)
        right_convert_cost = self.get_cost(s[::-1])[::-1]
        ans = int(1e11)
        for i in range(1,len(s)+1):
            cost0 = left_convert_cost[i][0] + right_convert_cost[i+1][0]
            cost1 = left_convert_cost[i][1] + right_convert_cost[i+1][1]
            ans = min(ans , min(cost0,cost1))
        return ans
