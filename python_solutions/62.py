class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Solution Overview
        # use dp to store the results and then update the next states
        cnt_path = [0 for col in range(n)]
        prev_path = cnt_path.copy()
        for row in range(m):
            for col in range(n):
                prev_path[col] = cnt_path[col]
                cnt_path[col] = 0
            for col in range(n):
                if row == 0 and col == 0:
                    cnt_path[col] = 1
                else:
                    if row-1 >= 0 :
                        cnt_path[col] += prev_path[col]
                    if col-1 >= 0 :
                        cnt_path[col] += cnt_path[col-1]
        return cnt_path[n-1]
