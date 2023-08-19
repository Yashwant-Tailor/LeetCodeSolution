class Solution:
    def get_all_possible_comb(self,grp):
        if len(grp)%2:
            return []
        if len(grp) == 0:
            return [[]]
        if len(grp) == 2:
            return [[grp]]
        comb1 = [[grp[0],grp[1]],[grp[2],grp[3]]]
        comb2 = [[grp[0],grp[2]],[grp[1],grp[3]]]
        comb3 = [[grp[0],grp[3]],[grp[2],grp[1]]]
        return [comb1,comb2,comb3]
    class graph:
        def __init__(self,n):
            self.node_cnt = n
            self.node_deg = [0 for i in range(n)]
        def add_edge(self,edge):
            a,b = edge
            a -= 1
            b -= 1
            self.node_deg[a] += 1
            self.node_deg[b] += 1
        def get_odd_deg_node_cnt(self):
            odd_cnt = 0
            grp = []
            for idx,deg in enumerate(self.node_deg):
                if deg%2:
                    odd_cnt += 1
                    grp.append(idx)
                if odd_cnt > 4:
                    return odd_cnt,grp
            return odd_cnt,grp
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:  
        # solution Overview
        # if we calculate the total number of nodes in the graph which has odd degree
        # then if our count is either 0 or 2 or 4 then only it is posiible to do with at most two additional edges to make every node degree even
        # if we have two nodes with odd degree 
        #       CASE1: these two node does not have any edge between them , in this case we can create a new edge between these two nodes 
        #        CASE2 : these two node have a edge between them, in this case if we have a node which does not share the edge with these two nodes ,then we can create two edge from two nodes with odd degree to this node (with even degree)
        # if we have four nodes with odd degree
        # we first divide these four nodes into all possible combination of two edges (two nodes in one edge)
        # a combination is valid edge combination if we don't have the edge already present in the edges (input)
        # if we don't have above case then it is not possible to make every node degree even
        gr = self.graph(n)
        for edge in edges:
            gr.add_edge(edge)
        odd_deg_cnt,grp = gr.get_odd_deg_node_cnt()
        
        if odd_deg_cnt%2:
            return False
        from collections import defaultdict
        n_node = defaultdict(set)
        for edge in edges:
            a,b = edge
            a -= 1
            b -= 1
            if a in grp:
                n_node[a].add(b)
            if b in grp:
                n_node[b].add(a)
        for new_edges in self.get_all_possible_comb(grp):
            is_pos = True
            for edge in new_edges:
                if edge[0] in n_node[edge[1]]:
                    if len(grp) == 4:
                        is_pos = False
                    union_grp_cnt = len(n_node[edge[0]].union(n_node[edge[1]]))
                    if n == union_grp_cnt:
                        is_pos = False
            if is_pos:
                return True
        return False

