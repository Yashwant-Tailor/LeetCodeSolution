class Solution:
    def get_neighbours(self,row,col,m,n):
        n_res = []
        if row-1>=0 :
            n_res.append([row-1,col])
        if col-1>=0:
            n_res.append([row,col-1])
        if row+1<m:
            n_res.append([row+1,col])
        if col+1<n:
            n_res.append([row,col+1])
        return n_res
    def minimumTime(self, grid: List[List[int]]) -> int:
        # Solution Overview
        # first let's consider the case when we can't move to bottom-right cell
        # it will be the case when we stands on the top-left cell and we can't make the first move (i.e. one of the adjacent cell does not have the time equal to either 0 or 1)
        # if we are able to make a move then its always possible to move to bottom-right corner
        # now if we arrive at the cell at time T1, and the required time to move to its adjacent cell is T2
        # if T2 <= T1+1 , then we can directly move to the adjacent cell
        # else T2 > T1 and diff = (T2-T1) is even then we need to wait for one extra second than the diff (because we need to make a move every second and difference is even and T2 is greater than T1 then after even move we will be at the cell where we arrived in time T1 and one more extra second will take to arrive the cell which has minimum time T2)
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        m , n = len(grid),len(grid[0])
        INF = int(1e6)
        min_time = [[INF for col in range(n)] for row in range(m)]
        import heapq as hp
        min_heap = []
        hp.heappush(min_heap,(0,0,0))
        while len(min_heap)>0:
            curr_time,row,col = hp.heappop(min_heap)
            for neighbour in self.get_neighbours(row,col,m,n):
                n_row,n_col = neighbour
                req_time = grid[n_row][n_col]
                diff = req_time-curr_time
                next_time = None
                if diff <= 1:
                    next_time = curr_time + 1
                else:
                    next_time = req_time
                    if diff%2 == 0:
                        next_time += 1
                if min_time[n_row][n_col] > next_time:
                    hp.heappush(min_heap,(next_time,n_row,n_col))
                    min_time[n_row][n_col] = next_time
        return min_time[m-1][n-1]
                    
                

            

