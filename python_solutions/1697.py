class Solution:
    class DisJointSet:
        def __init__(self,n):
            self.num_of_ver = n
            self.parent = [ver_num for ver_num in range(n)]
            self.rank = [1 for ver_num in range(n)]
        def join(self,u,v):
            pv = self.get_parent(v)
            pu = self.get_parent(u)
            if pv != pu:
                if self.rank[pv] > self.rank[pu]:
                    pu,pv = pv,pu
                self.parent[pv] = pu
                if self.rank[pv] == self.rank[pu]:
                    self.rank[pu] += 1
        def get_parent(self,ver):
            if ver == self.parent[ver]:
                return ver
            self.parent[ver] = self.get_parent(self.parent[ver])
            return self.parent[ver]
        def is_in_same_grp(self,u ,v):
            return self.get_parent(u) == self.get_parent(v)
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Solution Overview
        # we can sort the queries according to their limit
        # now use dis-joint set data structure , to keep track of maximum dis between two nodes 
        # if we at the a query with limit , then we will add all the edges which has dis < limit , and will see if p,q are in same set
        dst = self.DisJointSet(n)
        for idx in range(len(queries)):
            queries[idx].append(idx)
        queries.sort(key=lambda x : x[2])
        edgeList.sort(key=lambda x : x[2])
        edge_idx = 0
        query_idx = 0
        answer = []
        while query_idx < len(queries):
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < queries[query_idx][2]:
                u,v,dis = edgeList[edge_idx]
                dst.join(u,v)
                edge_idx += 1
            p,q,limit,idx = queries[query_idx]
            if dst.is_in_same_grp(p,q):
                answer.append((True,idx))
            else:
                answer.append((False,idx))
            query_idx += 1
        answer.sort(key=lambda x : x[1])
        for ans_idx in range(len(answer)):
            answer[ans_idx] = answer[ans_idx][0]
        return answer
