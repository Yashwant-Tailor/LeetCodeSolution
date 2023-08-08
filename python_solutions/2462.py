class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # Solution Overview
        # we can maintain a heap to get the minimum between candidates workers from first and last
        # if we pick a worker from first then we add another worker from the first end otherwise do the same thing for last end as well

        import heapq as hp
        min_heap = []
        class heap_node:
            def __init__(self,cost,idx,end):
                self.cost = cost
                self.idx = idx
                self.picked_end = end
            def __lt__(self,other):
                if other.cost == self.cost:
                    return self.cost < other.cost
                return self.cost < other.cost
        first_idx = 0
        last_idx = len(costs)-1
        while first_idx < candidates:
            hp.heappush(min_heap,heap_node(costs[first_idx],first_idx,'F'))
            first_idx += 1
        while last_idx >= first_idx and candidates >0:
            candidates -= 1
            hp.heappush(min_heap,heap_node(costs[last_idx],last_idx,'L'))
            last_idx -= 1
        total_cost = 0
        while k > 0:
            k -= 1
            min_cost_elm = hp.heappop(min_heap)
            total_cost += min_cost_elm.cost

            if first_idx <= last_idx:
                end = min_cost_elm.picked_end
                if end == 'F':
                    hp.heappush(min_heap,heap_node(costs[first_idx],first_idx,'F'))
                    first_idx += 1
                else:
                    hp.heappush(min_heap,heap_node(costs[last_idx],last_idx,'L'))
                    last_idx -= 1
        return total_cost

