class Solution:
    from math import floor,sqrt
    def isPos(self,ranks,cars,max_rep_time):
        cars_can_repaired = 0
        for rank in ranks:
            n2 = max_rep_time/rank
            n = floor(sqrt(n2))
            cars_can_repaired += n
        return cars_can_repaired >= cars
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Solution Overview
        # simply do a binary serach for minimum total repairing time 

        min_rep_time = 0
        max_rep_time = int(1e15)
        while min_rep_time < max_rep_time:
            mid = min_rep_time + (max_rep_time - min_rep_time)//2
            if self.isPos(ranks,cars,mid):
                max_rep_time = mid
            else:
                min_rep_time = mid+1
        return max_rep_time


