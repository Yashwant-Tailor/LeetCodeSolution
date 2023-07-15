class Solution:
    def get_neighbours(self,i,j,m,n):
        res = []
        if j+1 < n :
            res.append((i,j+1))
            if i-1>=0:
                res.append((i-1,j+1))
            if i+1 < m:
                res.append((i+1,j+1))
        return res
    def maxMoves(self, grid: List[List[int]]) -> int:
        # Solution Overview
        # traverse the matrix and use dynamic programming to store the maixmum number of moves we can till a particular cell (i,j)

        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for j in range(n)] for i in range(m)]

        ans = 0
        from collections import deque
        q = deque()
        # add initial positions from where we can start
        for i in range(m):
            q.append((i,0))
        while len(q) > 0:
            i , j = q.popleft()
            neighbours = self.get_neighbours(i,j,m,n)
            curr_move = dp[i][j]
            curr_val = grid[i][j]
            for neighbour in neighbours:
                nexti,nextj = neighbour
                neighbour_val = grid[nexti][nextj]
                if neighbour_val > curr_val and dp[nexti][nextj] < curr_move + 1:
                    dp[nexti][nextj] = curr_move + 1
                    ans = max(ans,dp[nexti][nextj])
                    q.append(neighbour)
        return ans
