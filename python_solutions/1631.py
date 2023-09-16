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
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        INF = int(1e7)
        import heapq as hp
        q = []
        vis = [[False for col in range(n)] for row in range(m)]
        effort = [[INF for col in range(n)] for row in range(m)]
        effort[0][0] = 0
        vis[0][0] = True
        q.append((0,(0,0)))
        while len(q)>0:
            curr_eff,loc = hp.heappop(q)
            row,col = loc
            vis[row][col] = True
            if row == m-1 and col == n-1:
                break
            for n_loc in self.get_neighbours(row,col,m,n):
                n_row,n_col = n_loc
                n_eff = max(curr_eff,abs(heights[row][col]-heights[n_row][n_col]))
                if not vis[n_row][n_col] and effort[n_row][n_col] > n_eff:
                    effort[n_row][n_col] = n_eff
                    hp.heappush(q,(n_eff,n_loc))
        return effort[m-1][n-1]
        
        

