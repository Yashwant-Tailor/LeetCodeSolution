class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Solution Overview
        # let say that 2nd mouse ate all the cheese and in this case final answer would be sum_reward (reward2[0]+reward[1]+ .... + reward2[n-1])
        # now let say at ith index instead of mouse2 , mouse1 eat the cheese
        # then our sum_reward needs an update and it would be 
        # sum_reward - reward2[i] + reward1[i] 
        # or (sum_reward + (reward1[i]-reward2[i]))
        # it is optimal to choose the first k maximum indices where we have (reward1[i]-reward2[i]) as sum_reward will be constant
        from queue import PriorityQueue
        class REWARD:
            def __init__(self,point1,point2):
                self.diff = point1-point2
            def __lt__(self,other_obj):
                return self.diff > other_obj.diff
        q = PriorityQueue()
        ans = 0
        for i in range(len(reward1)):
            ans += reward2[i]
            max_reward = max(reward1[i],reward2[i])
            q.put(REWARD(reward1[i],reward2[i]))
        while k > 0:
            k -= 1
            ans += q.get().diff
        return ans
