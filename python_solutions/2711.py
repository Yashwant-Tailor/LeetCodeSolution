class Solution:
    def update_matrix(self,grid,answer,x1,y1,x2,y2):
        idx_add = 0
        right_diagonal_dist = {}
        while x1 + idx_add < x2 and y1 + idx_add < y2:
            val = grid[x1+idx_add][y1+idx_add]
            if val in right_diagonal_dist:
                right_diagonal_dist[val] += 1
            else:
                right_diagonal_dist[val] = 1
            idx_add += 1
        idx_add = 0
        left_diagonal_dist = set()
        while x1 + idx_add < x2 and y1 + idx_add < y2:
            val = grid[x1+idx_add][y1+idx_add]
            right_diagonal_dist[val] -= 1
            if right_diagonal_dist[val] == 0:
                right_diagonal_dist.pop(val)
            answer[x1+idx_add][y1+idx_add] = abs(len(left_diagonal_dist)-len(right_diagonal_dist))
            idx_add += 1
            left_diagonal_dist.add(val)

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        # Solution Overview
        # for every diagonal just calculate the number of distinct element and update the answer matrix

        m , n = len(grid), len(grid[0])
        answer = [[0 for i in range(n)] for j in range(m)]
        for i in range(0,m):
            x1 , y1 = i , 0
            self.update_matrix(grid,answer,x1,y1,m,n)
        for j in range(1,n):
            x1 , y1 = 0 , j
            self.update_matrix(grid,answer,x1,y1,m,n)
        return answer
