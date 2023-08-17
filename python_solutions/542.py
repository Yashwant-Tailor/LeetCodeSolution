class Solution:
    class graph:
        def __init__(self,mat):
            self.mat = mat
            self.m = len(mat)
            self.n = len(mat[0])
            self.INF = int(1e5)
            self.dis_mat = [[self.INF for col in range(self.n)] for row in range(self.m)]

        def update_zero_loc(self,cor_q):
            for row in range(self.m):
                for col in range(self.n):
                    if self.mat[row][col] == 0:
                        cor_q.append((row,col))
                        self.dis_mat[row][col] = 0
            return
        def get_neighbour(self,cordinate):
            row,col = cordinate
            n_cor = []
            if row+1 < self.m:
                n_cor.append((row+1,col))
            if col+1 < self.n:
                n_cor.append((row,col+1))
            if row-1 >= 0:
                n_cor.append((row-1,col))
            if col-1 >= 0:
                n_cor.append((row,col-1))
            return n_cor
        def get_dis(self):
            from collections import deque
            cor_q = deque()
            self.update_zero_loc(cor_q)
            while len(cor_q) > 0:
                curr_cor = cor_q.popleft()
                row,col = curr_cor
                curr_dis = self.dis_mat[row][col]
                for n_cor in self.get_neighbour(curr_cor):
                    n_row,n_col = n_cor
                    if self.dis_mat[n_row][n_col] == self.INF:
                        self.dis_mat[n_row][n_col] = curr_dis + 1
                        cor_q.append((n_row,n_col))
            return self.dis_mat


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Solution Overview
        # simple BFS will give us the required distance from each cell
        # initially put all the cells having zero in the queue and then start the bfs
        gr = self.graph(mat)
        return gr.get_dis()
        
