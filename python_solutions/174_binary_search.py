class Solution:
    def isPos(self,mat,k_pow):
        m , n = len(mat),len(mat[0])
        pow_mat = [[0 for j in range(n)] for i in range(m)]
        vis = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    vis[i][j] = True
                    pow_mat[i][j] = k_pow + mat[i][j]
                if not vis[i][j]:
                    continue
                curr_pow = pow_mat[i][j]
                if curr_pow > 0:
                    if i+1 < m:
                        if not vis[i+1][j]:
                            pow_mat[i+1][j] = curr_pow + mat[i+1][j]
                            vis[i+1][j] = True
                        else:
                            pow_mat[i+1][j] = max(pow_mat[i+1][j],curr_pow + mat[i+1][j])
                    if j+1 < n:
                        if not vis[i][j+1]:
                            vis[i][j+1] = True
                            pow_mat[i][j+1] = curr_pow + mat[i][j+1]
                        else:
                            pow_mat[i][j+1] = max(pow_mat[i][j+1] , curr_pow + mat[i][j+1])
        if k_pow == 5:
            for row in pow_mat:
                print(row)
            print()
            for row in vis:
                print(row)
        if vis[m-1][n-1] and pow_mat[m-1][n-1] >0:
            return True
        return False
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # Solution Overview 
        # simple classic application of dynamic programming
        # fix the initial power of the knight (using binary search)
        # then find that with this initial power the knight can reach to the bottom or not
        min_pow = 0
        max_pow = 1000*200*200 + 1
        while min_pow + 1< max_pow:
            mid_pow = min_pow + (max_pow - min_pow)//2
            if self.isPos(dungeon,mid_pow):
                max_pow = mid_pow
            else:
                min_pow = mid_pow
        return max_pow
