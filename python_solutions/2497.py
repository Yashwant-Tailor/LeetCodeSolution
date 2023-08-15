class Solution:
    class node:
        def __init__(self,node_num,node_val):
            self.node_num = node_num
            self.node_val = node_val
            self.n_node_val = []
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        # Solution Overview
        # we can make star center to every vertex in the graph
        # now to make the start graph with at most k edges we will pick the edges connected to nodes having value greater the kth larges among all the neighbours
        nodes = []
        for i in range(len(vals)):
            nodes.append(self.node(i,vals[i]))
        for edge in edges:
            a,b = edge
            nodes[a].n_node_val.append(nodes[b].node_val)
            nodes[b].n_node_val.append(nodes[a].node_val)
        ans = nodes[0].node_val
        for i in range(len(vals)):
            nodes[i].n_node_val.sort()
            star_sum = nodes[i].node_val
            edge_inc = k
            n_node_val = nodes[i].n_node_val
            while edge_inc > 0 and len(n_node_val) > 0 and n_node_val[-1] > 0:
                star_sum += n_node_val.pop()
                edge_inc -= 1
            ans = max(ans,star_sum)
        return ans



