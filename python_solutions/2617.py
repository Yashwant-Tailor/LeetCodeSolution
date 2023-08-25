class Solution: 
    def is_reachable(self,loc1,loc2,grid):
        diff = (loc2[0] - loc1[0]) + (loc2[1] - loc1[1]) + grid[loc2[0]][loc2[1]]
        return diff >= 0
    def pop_row(self,row_heap,row,col,grid):
        import heapq as hp
        while len(row_heap)>0 and not self.is_reachable((row,col),(row,row_heap[0][1]),grid):
            hp.heappop(row_heap)
    def pop_col(self,col_heap,row,col,grid):
        import heapq as hp
        while len(col_heap)>0 and not self.is_reachable((row,col),(col_heap[0][1],col),grid):
            hp.heappop(col_heap)
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        # Solution Overview
        # if we reach at cell (i,j) in some moves (here we define moves at the count of visited cell)
        # then we will update the cost to reach to all the cell which are adjacent to it
        # for a cell (i,j) a adjacent cell will be as per the given condition in the problem statement
        # for each and col keep track of minimum moves of visited cell in that row or col, and to update (i,j) use these values
        m,n = len(grid),len(grid[0])
        INF = int(1e6)
        min_moves = [[INF for col in range(n)] for row in range(m)]
        min_moves[0][0] = 1
        import heapq as hp
        min_r = [[] for row in range(m)]
        min_c = [[] for col in range(n)]
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    hp.heappush(min_r[row],(1,0))
                    hp.heappush(min_c[col],(1,0))
                else:
                    self.pop_row(min_r[row],row,col,grid)
                    self.pop_col(min_c[col],row,col,grid)
                    curr_min_moves = INF
                    if len(min_r[row]) > 0:
                        curr_min_moves = min(curr_min_moves,min_r[row][0][0]+1)
                    if len(min_c[col]) > 0:
                        curr_min_moves = min(curr_min_moves,min_c[col][0][0]+1)
                    min_moves[row][col] = curr_min_moves
                    hp.heappush(min_r[row],(curr_min_moves,col))
                    hp.heappush(min_c[col],(curr_min_moves,row))
        return -1 if min_moves[m-1][n-1] == INF else min_moves[m-1][n-1]

