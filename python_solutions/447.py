class Solution:
    def dis(self,point1,point2):
        return (point1[0]-point2[0])**2 + (point1[1] - point2[1])**2
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        cnt = 0
        from collections import defaultdict
        dis_cnt = defaultdict(lambda : 0)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                dis_cnt[self.dis(points[i],points[j])] += 1
            for dis,curr_cnt in dis_cnt.items():
                cnt += (curr_cnt * (curr_cnt-1))
            dis_cnt.clear()
        return cnt

        
