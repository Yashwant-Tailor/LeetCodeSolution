class Solution:
    def get_neighbour(self,row,col,m,n):
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
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # Solution Overview
        # if we do simple bfs , for every cell , we store that how many can we reach the particular cell after removing some number of obstracle
        # i.e. dp[i][j][k] = will store that can we reach cell i,j after removing atmost k obstacles
        m,n = len(grid),len(grid[0])
        INF = int(1e6)
        short_path = [[[INF for idx in range(k+1)]for col in range(n)]for row in range(m)]
        from collections import deque
        loc_q = deque()
        loc_q.append((0,0,0))
        short_path[0][0][0] = 0
        while len(loc_q) > 0:
            row,col,removed_obstcl = loc_q.popleft()
            curr_short_path = short_path[row][col][removed_obstcl]
            for n_loc in self.get_neighbour(row,col,m,n):
                n_row,n_col = n_loc
                n_removed_obstcl = removed_obstcl + grid[n_row][n_col]
                if n_removed_obstcl <= k and short_path[n_row][n_col][n_removed_obstcl] > curr_short_path+1:
                    short_path[n_row][n_col][n_removed_obstcl] = curr_short_path+1
                    loc_q.append((n_row,n_col,n_removed_obstcl))
        min_short_path = min(short_path[m-1][n-1])
        return -1 if min_short_path == INF else min_short_path


