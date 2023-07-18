class Solution:
    def get_neighbours(self,i,j,m,n):
        neighbours = []
        if i-1 >= 0 :
            neighbours.append([i-1,j])
        if j-1 >= 0:
            neighbours.append([i,j-1])
        if i+1 < m:
            neighbours.append([i+1,j])
        if j+1 < n:
            neighbours.append([i,j+1])
        return neighbours
    def get_fish_count(self,i,j,m,n,vis,grid):
        total_fish_count = grid[i][j]
        vis[i] |= (1<<j)
        neighbours = self.get_neighbours(i,j,m,n)
        for neighbour in neighbours:
            ni,nj = neighbour
            if grid[ni][nj] != 0 and (vis[ni] & (1<<nj)) == 0:
                total_fish_count += self.get_fish_count(ni,nj,m,n,vis,grid)
        return total_fish_count
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # Solution Overview
        # use dfs to find the maximum fish can be collected if we start at current cell
        ans = 0
        m , n = len(grid),len(grid[0])
        vis = [0 for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                if (vis[i] & (1<<j)) != 0:
                    continue
                curr_fish_count = self.get_fish_count(i,j,m,n,vis,grid)
                ans = max(ans , curr_fish_count)
        return ans
            
