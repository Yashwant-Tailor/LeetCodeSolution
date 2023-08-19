class Solution:
    class city_network : 
        def __init__(self,n):
            self.num_of_city = n
            self.n_city = [set() for i in range(n)]
        def add_road(self,road):
            a,b = road
            self.n_city[a].add(b)
            self.n_city[b].add(a)
        def get_max_deg_ver_cnt(self):
            max_deg1 ,max_deg2 = -1,-1
            for n_cities in self.n_city:
                city_deg = len(n_cities)
                if city_deg > max_deg1:
                    max_deg2 = max_deg1
                    max_deg1 = city_deg
                elif max_deg2 <= city_deg <= max_deg1:
                    max_deg2 = city_deg
            return max_deg1,max_deg2
        def get_ver_with_deg(self,deg):
            deg_grp = []
            for city_num,n_cities in enumerate(self.n_city):
                city_deg = len(n_cities)
                if city_deg == deg:
                    deg_grp.append(city_num)
            return deg_grp
        def get_maximum_network_rank(self):
            max_deg1,max_deg2 = self.get_max_deg_ver_cnt()
            max_deg_grp1 = self.get_ver_with_deg(max_deg1)
            max_deg_grp2 = self.get_ver_with_deg(max_deg2)
            is_deg_eq = max_deg1 == max_deg2
            for idx1 in range(len(max_deg_grp1)):
                for idx2 in range(idx1,len(max_deg_grp2)):
                    if is_deg_eq and idx1 == idx2:
                        continue
                    city1 = max_deg_grp1[idx1]
                    city2 = max_deg_grp2[idx2]
                    is_direct_conn = (city1 in self.n_city[city2])
                    if not is_direct_conn:
                        return max_deg1 + max_deg2
            return max_deg1 + max_deg2 - 1
                    

    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Solution Overview
        # if we calculate the degree of each vertex in the graph , then the maximum possible rank will be when we take the two vertex with the highest degree
        # there can be two case
        # CASE1 : we have more than two vertex with highest degree in the graph
        #       in this case our answer could be (2*highest_degree OR 2*highest_degree - 1)
        #       first answer is possible when we have two vertex with no edge between these two vertex
        #       otherwise second answer is always possible
        # CASE2 : we have one vetex with highest degree , and one or more vertex with second highest degree
        #       in this case we again have two possible answers (highest_degree + second_highest_degree OR highest_degree + second_highest_degree - 1)
        #       first answer is only possible if we have no edge between highest_degree vertex and second highest degree vertex
        #       otherwise second answer is always possible
        cn = self.city_network(n)
        for road in roads:
            cn.add_road(road)
        return cn.get_maximum_network_rank()

