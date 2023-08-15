class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # Solution Overview
        # we can pre calculate the number of zeros and ones in given row or column
        m = len(grid)
        n = len(grid[0])
        row_cnt = [[0,0] for i in range(m)]
        col_cnt = [[0,0] for j in range(n)]
        for i in range(m):
            for j in range(n):
                row_cnt[i][0] += grid[i][j] ^ 1
                row_cnt[i][1] += grid[i][j] & 1
                col_cnt[j][0] += grid[i][j] ^ 1
                col_cnt[j][1] += grid[i][j] & 1
        diff = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = row_cnt[i][1] + col_cnt[j][1] - row_cnt[i][0] - col_cnt[j][0]
        return diff

