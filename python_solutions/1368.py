class Solution:
    def get_neighbours(self,row,col,m,n):
        res = []
        if row-1>=0:
            res.append((row-1,col))
        if col-1>=0:
            res.append((row,col-1))
        if row+1<m:
            res.append((row+1,col))
        if col+1<n:
            res.append((row,col+1))
        return res
    def get_next_loc(self,row,col,grid):
        n_row,n_col = row,col
        if grid[row][col] == 1:
            n_col += 1
        elif grid[row][col] == 2:
            n_col -= 1
        elif grid[row][col] == 3:
            n_row += 1
        else :
            n_row -= 1
        return n_row,n_col
    def minCost(self, grid: List[List[int]]) -> int:
        # Solution Overview
        # each arrow direction initailly creates , an connected component , we can connect two component by adjusting the arrow direction with cost = 1, 
        # we can find the optimal cost using BFS
        m,n = len(grid),len(grid[0])
        self.INF = m*n + 1
        cost = [[self.INF for col in range(n)] for row in range(m)]
        cost[0][0] = 0
        from collections import deque
        loc_q = deque()
        loc_q.append((0,0,0))
        while len(loc_q)>0:
            row,col,curr_cost = loc_q.popleft()
            arrow_loc = self.get_next_loc(row,col,grid)
            for n_loc in self.get_neighbours(row,col,m,n):
                n_row,n_col = n_loc
                n_cost = curr_cost
                if n_loc != arrow_loc:
                    n_cost += 1
                if cost[n_row][n_col] > n_cost:
                    cost[n_row][n_col] = n_cost
                    loc_q.append((n_row,n_col,n_cost))
        return cost[m-1][n-1]

