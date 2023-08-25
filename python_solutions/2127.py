class Solution:
    class graph :
        def __init__(self,favorite):
            self.emp_cnt = len(favorite)
            self.next_emp = favorite
            self.n_emps = [set() for emp in range(self.emp_cnt)]
            for emp,fav in enumerate(favorite):
                self.n_emps[emp].add(fav)
                self.n_emps[fav].add(emp)
            self.dis = {}
            for emp in range(self.emp_cnt):
                self.dis[emp] = -3
            self.cycle_ends = [] 
            self.comp = set()
            self.parent = [-1 for emp in range(self.emp_cnt)]
        def get_comp(self,emp):
            self.dis[emp] = -2
            self.comp.add(emp)
            for n_emp in self.n_emps[emp]:
                if self.dis[n_emp] == -3:
                    self.get_comp(n_emp)
        def find_cycle(self,emp):
            if self.dis[emp] > 0:
                return self.dis[emp]
            self.dis[emp] = -1
            next_emp = self.next_emp[emp]
            if self.dis[next_emp] == -1:
                # we have found the cycle with emp and next_emp as cycle ends
                self.cycle_ends.append(emp)
                self.cycle_ends.append(next_emp)
                self.dis[emp] = 1
            elif self.dis[next_emp] == -2:
                self.dis[emp] = self.find_cycle(next_emp) + 1
            else:
                self.dis[emp] = self.dis[next_emp] + 1
            return self.dis[emp]
        def reset_dis(self):
            for emp in self.comp:
                self.dis[emp] = -1
        def find_dis(self,emp):
            next_emp = self.next_emp[emp]
            if self.dis[emp] == -1:
                self.parent[emp],self.dis[emp] = self.find_dis(next_emp)
                self.dis[emp] += 1
            return self.parent[emp],self.dis[emp]
        def get_max_dis(self):
            self.reset_dis()
            end1,end2 = self.cycle_ends
            self.dis[end1] = 0
            self.dis[end2] = 0
            self.parent[end1] = end1
            self.parent[end2] = end2
            max_dis_end1 = 0
            max_dis_end2 = 0
            for emp in self.comp:
                if self.dis[emp] == -1:
                    par,curr_dis = self.find_dis(emp)
                    if par == end1:
                        max_dis_end1 = max(max_dis_end1,curr_dis)
                    else:
                        max_dis_end2 = max(max_dis_end2,curr_dis)
            return max_dis_end1 + max_dis_end2
        def get_cycle_len(self):
            end1,end2 = self.cycle_ends
            return self.dis[end1]+self.dis[end2]-1
        def get_inv_emp_cnt(self,start_emp):
            self.cycle_ends = []
            self.comp = set()
            self.get_comp(start_emp)
            self.find_cycle(start_emp)
            cycle_len = self.get_cycle_len()
            if cycle_len == 2:
                return True,self.get_max_dis() + 2
            return False,cycle_len
        def get_max_inv_emp_cnt(self):
            length_2 = 0
            length_gre_2 = 0
            for emp in range(self.emp_cnt):
                if self.dis[emp] == -3:
                    is_length_2,ans = self.get_inv_emp_cnt(emp)
                    if is_length_2:
                        length_2 += ans
                    else:
                        length_gre_2 = max(length_gre_2,ans)
            return max(length_2,length_gre_2)
    def maximumInvitations(self, favorite: List[int]) -> int:
        # Solution Overview
        # if we create the directed graph with from vertext i to vertex favorite[i]
        # then the maximum employee , who can sit in the round table , is the lenth of the cycle in this graph (in this graph we will always have one cycle)
        # if length of the cycle is two then we can let candidates outside the cycle to sit next to one of the person in the cycle , which is favorite to them
        # if length is greater than 2 , then answer will always be cycle length

        gr = self.graph(favorite)
        return gr.get_max_inv_emp_cnt()
