class Solution:
    class city:
        def __init__(self,city_num):
            self.city_num = city_num
            self.n_city = []
            self.vis = False
        def get_neighbour(self):
            return self.n_city
    def DFS(self,city_num,cities,con_comp):
        cities[city_num].vis = True
        for n_city in cities[city_num].get_neighbour():
            n_city_num , n_city_dis = n_city
            if not cities[n_city_num].vis:
                self.DFS(n_city_num,cities,con_comp)
        con_comp.append(city_num)
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Solution Overview
        # if we have a connected components then we can visit any city in this connected component (as roads are bidirectional)
        # now to minimize the score we should traverse the edge in this connected component which has minimum value
        # as per given constraints in the question we will always have the path between 1 to n
        # that means we need to find that connected component and return the minimum distance from the all edges (roads) we have in this connected component
        cities = []
        for i in range(n):
            cities.append(self.city(i))
        for road in roads:
            a,b,dis = road
            cities[a-1].n_city.append([b-1,dis])
            cities[b-1].n_city.append([a-1,dis])
        con_comp = []
        self.DFS(0,cities,con_comp)
        ans = cities[0].n_city[0][1]
        for curr_city in con_comp:
            for n_city in cities[curr_city].get_neighbour():
                n_city_num,n_city_dis = n_city
                ans = min(ans,n_city_dis)
        return ans


