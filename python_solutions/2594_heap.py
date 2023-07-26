class Solution:
    def get_time_taken(self,mechanic):
        r  = mechanic.rank
        n = mechanic.cars_repaired
        return r * n * n
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # Solution Overview
        # for a mechaninc repairing n cars, the time it would take to repair one more car (total number of cars that mechaninc would have is n+1) is  
        # r * n^2 (to repair n cars) + r * (2*n+1) (to repair one more car)
        # from here it clear that we will put the ith car to a mechanic which will have r * (2*n+1) {this mechaninc is already repairing n cars} as minimum value
        # to maintain this value we can take help of priority queue

        from queue import PriorityQueue
        from dataclasses import dataclass,field
        time_to_rep = PriorityQueue()
        @dataclass(order=True)
        class MECHANIC:
            rank : int = field(compare=False)
            cars_repaired : int = field(compare=False)
            total_time_to_repair : int = field(compare=True)
        # a mechanic would take r time repair their first car
        for rank in ranks:
            time_to_rep.put(MECHANIC(rank,0,rank))
        cars_to_repair = cars
        ans = None
        while cars_to_repair > 0:
            cars_to_repair -= 1
            # for this car get the mechaninc which taken minimum time to repair one more car
            mechanic_with_min_time = time_to_rep.get()
            if ans is not None:
                ans = max(ans,mechanic_with_min_time.total_time_to_repair)
            else:
                ans = mechanic_with_min_time.total_time_to_repair
            # update the number of cars this mechaninc repaired so far
            mechanic_with_min_time.cars_repaired  += 1

            # update the total time which this mechanic would take to repair one more car , along with the cars repaired so far
            r = mechanic_with_min_time.rank
            n = mechanic_with_min_time.cars_repaired + 1
            new_total_time_to_repair = r * n * n
            
            mechanic_with_min_time.total_time_to_repair = new_total_time_to_repair

            # put mechanic back into the priority queue
            time_to_rep.put(mechanic_with_min_time)
        # as all mechanic can work parallely max time would be maximum out of all the mechanics time taken
        
        return ans


