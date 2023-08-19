class Solution:
    class graph:
        def __init__(self,n):
            self.num_of_ver = n
            self.vertices = [[] for i in range(n)]
            self.INF = int(1e5)
            self.initialize_graph()
        def initialize_graph(self):
            self.ver_dis = [self.INF for i in range(self.num_of_ver)]
            self.parent = [-1 for i in range(self.num_of_ver)]
        def flush_graph(self):
            for ver_num in range(self.num_of_ver):
                self.ver_dis[ver_num] = self.INF
                self.parent[ver_num] = -1
        def add_edge(self,edge):
            u,v = edge
            self.vertices[u].append(v)
            self.vertices[v].append(u)
        def get_shortest_cycle_len(self,start_ver):
            from collections import deque
            ver_q = deque()
            ver_q.append(start_ver)
            self.ver_dis[start_ver] = 1
            cycle_len = self.INF
            self.parent[start_ver] = start_ver
            while len(ver_q) > 0:
                curr_ver = ver_q.popleft()
                for n_ver in self.vertices[curr_ver]:
                    if self.parent[curr_ver] == n_ver:
                        continue
                    if self.parent[n_ver] != -1:
                        curr_cycle_len = self.ver_dis[curr_ver] + self.ver_dis[n_ver] - 1
                        cycle_len = min(cycle_len,curr_cycle_len)
                    else:
                        self.ver_dis[n_ver] = self.ver_dis[curr_ver]+1
                        self.parent[n_ver] = curr_ver
                        ver_q.append(n_ver)
            return cycle_len
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # Solution Overview
        # find the cycle in the graph(using BFS) and then update the minimum length of the cycle
        gr = self.graph(n)
        for edge in edges:
            gr.add_edge(edge)
        shortest_cycle_len = gr.INF
        for ver_num in range(n):
            cycle_len = gr.get_shortest_cycle_len(ver_num)
            gr.flush_graph()
            shortest_cycle_len = min(shortest_cycle_len,cycle_len)
        return -1 if shortest_cycle_len == gr.INF else shortest_cycle_len


