class Solution:
    def get_neighbour(self,row,col,m,n):
        res = []
        if row+1 < m:
            res.append([row+1,col])
        if col+1 < n:
            res.append([row,col+1])
        return res
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Solution Overview
        # simply use dynamic programing to store the state (number of unique paths till index [i,j], where i denote the ith row and j denotes the jth column)
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        path_count = [[0 for j in range(n)] for i in range(m)]
        path_count[0][0] = obstacleGrid[0][0] ^ 1 # Base Case
        for row in range(m):
            for col in range(n):
                if obstacleGrid[row][col] == 1:
                    continue
                for neighbour in self.get_neighbour(row,col,m,n):
                    n_row,n_col = neighbour
                    if obstacleGrid[n_row][n_col] == 0:
                        path_count[n_row][n_col] += path_count[row][col]
        return path_count[m-1][n-1]
