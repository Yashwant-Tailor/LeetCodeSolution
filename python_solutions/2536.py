class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # Solution Overview
        # it is not efficient to update value for every cell in a submatrix for a given query
        # but we can at least update the value for rows and use the range sum technique to find the sum for column

        ans_mat = [[0 for j in range(n)] for i in range(n)]
        for query in queries:
            row1,col1, row2,col2 = query
            for rowi in range(row1,row2+1):
                ans_mat[rowi][col1] += 1
                if col2 + 1 < n:
                    ans_mat[rowi][col2+1] -= 1
        for rowi in range(n):
            curr_row_sum = 0
            for coli in range(n):
                curr_row_sum += ans_mat[rowi][coli]
                ans_mat[rowi][coli] = curr_row_sum
        return ans_mat
