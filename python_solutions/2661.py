class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Solution overview
        # for each row and column keep track of painted cell 
        # at any time if we see that a row or column is completely painted 
        # we will declare that index is our final answer
        m,n = len(mat),len(mat[0])
        row_unp_cell_count = [n for i in range(m)]
        col_unp_cell_count = [m for i in range(n)]
        # to quickly get the index of number in mat build a hash map 
        # where key will be number and value will be location (i,j) in mat for that number
        hashmap = {}
        for i in range(m):
            for j in range(n):
                hashmap[mat[i][j]] = (i,j)
        ans = len(arr)-1
        for idx,num in enumerate(arr):
            i,j = hashmap[num]
            row_unp_cell_count[i] -= 1
            if row_unp_cell_count[i] == 0:
                ans = idx
                break
            col_unp_cell_count[j] -= 1
            if col_unp_cell_count[j] == 0:
                ans = idx
                break
        return ans

