class Solution:
    class graph :
        def __init__(self,n):
            self.num_of_ver = n
            self.n_vers = [[] for i in range(n)]
            self.grp_num = [-2 for i in range(n)]
            self.curr_comp = []
            from collections import deque
            self.ver_q = deque()
        def add_edge(self,edge):
            a,b = edge
            a -= 1
            b -= 1
            self.n_vers[a].append(b)
            self.n_vers[b].append(a)
        def get_connected_comp(self,ver):
            self.grp_num[ver] = -1
            for n_ver in self.n_vers[ver]:
                if self.grp_num[n_ver] == -2:
                    self.get_connected_comp(n_ver)
            self.curr_comp.append(ver)
        def make_group(self,start_ver):
            self.ver_q.append(start_ver)
            self.grp_num[start_ver] = 1
            max_grp_cnt = 0
            while len(self.ver_q) > 0:
                curr_ver = self.ver_q.popleft()
                curr_ver_grp_num = self.grp_num[curr_ver]
                max_grp_cnt = max(max_grp_cnt,curr_ver_grp_num)
                for n_ver in self.n_vers[curr_ver]:
                    if self.grp_num[n_ver] == curr_ver_grp_num-1 or self.grp_num[n_ver] == curr_ver_grp_num + 1:
                        continue
                    if self.grp_num[n_ver] == -1:
                        self.ver_q.append(n_ver)
                        self.grp_num[n_ver] = curr_ver_grp_num + 1
                    else:
                        return -1
            return max_grp_cnt
        def reset_grp_num(self):
            for ver in self.curr_comp:
                self.grp_num[ver] = -1
        def get_max_group_cnt(self,start_ver):
            self.curr_comp = []
            self.get_connected_comp(start_ver)
            max_grp_cnt = 0
            for ver in self.curr_comp:
                grp_cnt = self.make_group(ver)
                if grp_cnt == -1:
                    return -1
                max_grp_cnt = max(max_grp_cnt,grp_cnt)
                self.reset_grp_num()
            return max_grp_cnt
            

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Solution Overview
        # graph should be bipartite 
        # if we fix a group for any node then its neighbour will be in next group and their neighbours in next group but if we have any next.next.next....neighbour which is adjacent to any previousaly allocated group (except for its parent) then we can't have bipartite coloring of our graph
        # to find the maximum length in a connected component 
        # we first fix a vertex in the leftmost group and from there we start allocating next group to its neighbour , finally we will have maximum number of group we can have with this vertex placed at the leftmost group
        # we will do this operation for every vertex in the group ,and take the maximum groups we can get 


        gr = self.graph(n)
        for edge in edges:
            gr.add_edge(edge)
        total_grp_cnt = 0
        for ver_num in range(n):
            if gr.grp_num[ver_num] == -2:
                curr_grp_cnt = gr.get_max_group_cnt(ver_num)
                if curr_grp_cnt == -1:
                    return -1
                total_grp_cnt += curr_grp_cnt
        return total_grp_cnt

