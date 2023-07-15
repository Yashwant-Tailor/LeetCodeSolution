class Solution:
    def dfs(self,ver,vis,graph,connected_comp):
        vis[ver] = True
        connected_comp.append(ver)
        for neighbour in graph[ver]:
            if not vis[neighbour]:
                self.dfs(neighbour,vis,graph,connected_comp)
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Solution Overview
        # find the connected component 
        # for each component check that each vertes has the degree == length of conncted component - 1

        graph = [[] for i in range(n)]
        for edge in edges:
            a,b = edge
            graph[a].append(b)
            graph[b].append(a)
        ans = 0
        vis = [False for i in range(n)]
        for i in range(n):
            if not vis[i]:
                connected_comp = []
                self.dfs(i,vis,graph,connected_comp)
                is_complete_connected_comp = True
                for ver in connected_comp:
                    is_complete_connected_comp &= (len(graph[ver]) == len(connected_comp)-1)
                if is_complete_connected_comp:
                    ans += 1
        return ans
