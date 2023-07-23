class Solution:
    def get_cost(self,x1,y1,x2,y2):
        return abs(x2-x1) + abs(y2-y1)
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # Solution Overview
        # make the wieghted graph and find the minimum distance using dikjstra's algorithm
        # How to make graph ?
        # from start to every special road starting point we will have have edge (weight can be calculate using the given cordinates)
        # from every speacial road ending point we will have an edge to target and all other special road starting point (except the starting point for the given eding point)
        from collections import defaultdict
        adj = defaultdict(list)
        start = (start[0],start[1])
        cost = self.get_cost(start[0],start[1],target[0],target[1])
        target = (target[0],target[1])
        # make an edge from start to target
        adj[start].append((target[0],target[1],cost))
        for idx,special_road in enumerate(specialRoads):
            cost = self.get_cost(start[0],start[1],special_road[0],special_road[1])
            edge = (special_road[0],special_road[1],cost)
            # make an edge from start to special road starting point
            adj[start].append(edge)
            # make an edge from special road starting point to ending point
            edge = (special_road[2],special_road[3],special_road[4])
            adj[(special_road[0],special_road[1])].append(edge)
            # make an edge from special road ending point to target
            cost = self.get_cost(target[0],target[1],special_road[2],special_road[3])
            edge = (target[0],target[1],cost)
            adj[(special_road[2],special_road[3])].append(edge)
            # make an edge from the special road ending point to starting point of every other special road
            for next_idx,next_special_road in enumerate(specialRoads):
                if next_idx == idx:
                    continue
                cost = self.get_cost(next_special_road[0],next_special_road[1],special_road[2],special_road[3])
                edge = (next_special_road[0],next_special_road[1],cost)
                adj[(special_road[2],special_road[3])].append(edge)
        # let's keep the distance of start point from the all other points in one hashmap
        dis = defaultdict(lambda : int(1e18)) # Initiallize to Infinity Distance
        dis[start] = 0
        # create an priority queue to keep track of next node to choose for dikjstra's relaxation
        from queue import PriorityQueue
        from dataclasses import dataclass,field
        from typing import Any
        @dataclass(order=True)
        class node:
            cost : int = field(compare=True)
            point : Any = field(compare=False)
        q = PriorityQueue()
        q.put(node(0,start))
        while not q.empty():
            curr_node = q.get()
            cur_dis = curr_node.cost
            curr_point = curr_node.point
            for neighbour in adj[curr_point]:
                n_point = (neighbour[0],neighbour[1])
                cost = neighbour[2]
                if dis[n_point] > cur_dis + cost :
                    dis[n_point] = cur_dis + cost
                    q.put(node(dis[n_point],n_point))
        return dis[target]



        
