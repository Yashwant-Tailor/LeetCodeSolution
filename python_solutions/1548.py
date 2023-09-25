class Solution:
    def man_dis(self,p1,p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        picked_idx = set()
        INF = int(1e12)
        dis = [INF for idx in range(len(points))]
        dis[0] = 0
        total_cost = 0
        for itr in range(0,len(points)):
            min_dis_idx = None
            min_dis = INF
            for idx,curr_dis in enumerate(dis):
                if idx not in picked_idx and min_dis > curr_dis:
                    min_dis = curr_dis
                    min_dis_idx = idx
            picked_idx.add(min_dis_idx)
            total_cost += min_dis
            for idx in range(len(points)):
                if idx not in picked_idx:
                    dis[idx] = min(dis[idx],self.man_dis(points[idx],points[min_dis_idx]))
        return total_cost
        
