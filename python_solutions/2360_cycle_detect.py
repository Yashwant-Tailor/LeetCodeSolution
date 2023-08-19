class Solution:
    class node:
        def __init__(self,node_num):
            self.node_num = 0
            self.n_node = []
            self.longest_cycle_len = 0
            self.color = 'W'
            self.node_cnt = 0
    def DFS(self,node_num,nodes,path_node_cnt):
        nodes[node_num].color = 'G'
        nodes[node_num].node_cnt = path_node_cnt
        for n_node in nodes[node_num].n_node:
            if nodes[n_node].color == 'W':
                self.DFS(n_node,nodes,path_node_cnt+1)
            elif nodes[n_node].color == 'G':
                cycle_len = path_node_cnt + 1 - nodes[n_node].node_cnt
                nodes[n_node].longest_cycle_len  = cycle_len
        nodes[node_num].color = 'B'
        
    def longestCycle(self, edges: List[int]) -> int:
        # Solution Overview
        # detect the cycly in the given graph
        n = len(edges)
        nodes = []
        for i in range(n):
            nodes.append(self.node(i))
            if edges[i] != -1:
                nodes[-1].n_node.append(edges[i])
        for i in range(n):
            if nodes[i].color == 'W':
                self.DFS(i,nodes,0)
        long_cycle_len = 0
        for i in range(n):
            long_cycle_len = max(long_cycle_len,nodes[i].longest_cycle_len)
        if long_cycle_len == 0:
            return -1
        return long_cycle_len


