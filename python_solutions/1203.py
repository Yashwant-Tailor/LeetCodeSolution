class Solution:
    class TopoSort:
        def __init__(self,ver_list,edges_list):
            self.ver_list = ver_list
            self.edges_list = edges_list
        def create_graph(self):
            from collections import defaultdict
            self.gr = defaultdict(list)
            for edge in self.edges_list:
                u,v = edge
                self.gr[u].append(v)
            self.color = defaultdict(lambda : 'W')
        def find_cycle(self,ver_num):
            self.color[ver_num] = 'G'
            for n_ver in self.gr[ver_num]:
                if self.color[n_ver] == 'G':
                    return True
                elif self.color[n_ver] == 'W':
                    if self.find_cycle(n_ver):
                        return True
            self.color[ver_num] = 'B'
            self.topo_order.append(ver_num)
            return False
        def get_topological_sorting(self):
            self.create_graph()
            self.topo_order = []
            for ver_num in self.ver_list:
                if self.color[ver_num] == 'W':
                    if self.find_cycle(ver_num):
                        return False,[]
            self.topo_order.reverse()
            return True,self.topo_order

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # Solution Overview
        # first we group each element 
        # next based on the dependency find the right order of groups in the sorted array (we can use topological sorting)
        # once we have the right ordering of groups in sorted array, next we need to consider the ordering of elements within same group , again we will take help of dependecies to find the right ordering within the group 
        # we are successfully able to find the right group and element ordering within the group then we have a sorted list , otherwise it is not possible to create one sorted list
        item_grp_num = [None for item in range(n)]
        not_in_group_num = m+1
        from collections import defaultdict
        groups = defaultdict(list)
        for idx,group_num in enumerate(group):
            if group_num == -1:
                group_num = not_in_group_num
                not_in_group_num += 1
            item_grp_num[idx] = group_num
            groups[group_num].append(idx)
        group_edges = []
        from collections import defaultdict
        within_grp_edges = defaultdict(list)
        for item in range(n):
            item_grp = item_grp_num[item]
            for before_item in beforeItems[item]:
                before_item_grp = item_grp_num[before_item]
                if item_grp != before_item_grp:
                    group_edges.append([before_item_grp,item_grp])
                else:
                    within_grp_edges[item_grp].append([before_item,item])
        can_order , group_ordering = self.TopoSort([group_num for group_num in range(not_in_group_num)],group_edges).get_topological_sorting()
        if not can_order:
            return []
        for grp_num,same_grp_edges in within_grp_edges.items():
            can_order,groups[grp_num] = self.TopoSort(groups[grp_num],within_grp_edges[grp_num]).get_topological_sorting()
            if not can_order:
                return []
        sorted_list = []
        for grp_num in group_ordering:
            sorted_list += groups[grp_num]
        return sorted_list
        

