class Solution:
    class DisjointSet:
        def __init__(self,n):
            self.num_of_ver = n
            self.parent = [i for i in range(n)]
            self.rank = [0 for i in range(n)]
        def get_parent(self,ver):
            if self.parent[ver] == ver:
                return ver
            self.parent[ver] = self.get_parent(self.parent[ver])
            return self.parent[ver]
        def is_same_parent(self,ver1,ver2):
            return self.get_parent(ver1) == self.get_parent(ver2)
        def join_set(self,a,b):
            parent_a = self.get_parent(a)
            parent_b = self.get_parent(b)
            if parent_a != parent_b:
                if self.rank[parent_a] < self.rank[parent_b]:
                    parent_a,parent_b = parent_b , parent_a
                self.parent[parent_b] = parent_a
                if self.rank[parent_a] == self.rank[parent_b]:
                    self.rank[parent_a] += 1

    class Critical : 
        def __init__(self,n,edges):
            self.num_of_ver = n
            self.edges = [[edge,idx] for idx,edge in enumerate(edges)]
            self.edges.sort(key = lambda x : x[0][2])
            self.mst_edges = []
        def get_mst_weight(self,removed_edge_idx):
            total_weight = 0
            self.mst_edges.clear()
            ver_grp = Solution.DisjointSet(self.num_of_ver)
            total_iteration = self.num_of_ver-1
            for edge in self.edges:
                if edge[1] == removed_edge_idx:
                    continue
                ver1,ver2,weight = edge[0]
                if not ver_grp.is_same_parent(ver1,ver2):
                    total_iteration -= 1
                    total_weight += weight
                    self.mst_edges.append(edge)
                    ver_grp.join_set(ver1,ver2)
                if total_iteration == 0:
                    break
            return total_weight

    class PseudoCritical:
        def __init__(self,n,edges,mst_edges):
            self.edges = edges.copy()
            self.mst_edges = mst_edges
            self.num_of_ver = n
            self.vis = [False for i in range(len(edges))]
            for edge in mst_edges:
                self.vis[edge[1]] = True
        def get_same_weight_edge(self,weight):
            res = []
            for idx,edge in enumerate(self.edges):
                if edge[2] == weight and not self.vis[idx]:
                    res.append([edge,idx])
            return res
        def make_two_component(self,mst_edge):
            ver_grp = Solution.DisjointSet(self.num_of_ver)
            for curr_mst_edge in self.mst_edges:
                if mst_edge == curr_mst_edge:
                    continue
                ver1,ver2,weight = curr_mst_edge[0]
                ver_grp.join_set(ver1,ver2)
            return ver_grp
        def get_pseudo_edge(self,mst_edge):
            ver_grp = self.make_two_component(mst_edge)
            weight = mst_edge[0][2]
            pseudo_edge = set()
            same_weight_edges = self.get_same_weight_edge(weight)
            for same_weight_edge in same_weight_edges:
                ver1,ver2,weight = same_weight_edge[0]
                if not ver_grp.is_same_parent(ver1,ver2):
                    pseudo_edge.add(same_weight_edge[1])
            return pseudo_edge
                 
            
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Solution Overview
        # first find the mst (we will know the total weight of the mst)
        # How to find the Pseudo Critical Edge
        # in the mst , for each edge --> remove that edge , after removal we will have two component , now the edge with the same weight as removed edge , and it is not taken in our MST will be a Pseudo Critical Edge
        # How to find the Critical Edge
        # iterate over each edge in edges , remove that edge and find the mst with remaining edges, if the weight of the MST is increased then its critical edge
        gr = self.Critical(n,edges)
        total_mst_weight = gr.get_mst_weight(len(edges)+1)
        mst_edges = gr.mst_edges.copy()
        # Handling for critical edges
        critical_edges = []
        for idx in range(len(edges)):
            curr_mst_weight = gr.get_mst_weight(idx)
            
            if curr_mst_weight != total_mst_weight:
                critical_edges.append(idx)
        # Handling for non critical edges
        non_critical_edges = set()
        pseudo_critical = self.PseudoCritical(n,edges,mst_edges)
        for edge in mst_edges:
            ver1,ver2,weight = edge[0]
            curr_non_critical = pseudo_critical.get_pseudo_edge(edge)
            non_critical_edges = non_critical_edges.union(curr_non_critical)
            if len(curr_non_critical)>0:
                non_critical_edges.add(edge[1])
        non_critical_edges = list(non_critical_edges) 
        return [critical_edges,non_critical_edges]
