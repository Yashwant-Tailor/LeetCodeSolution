class Solution:
    def __init__(self):
        self.next_loc_add = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
    def get_neighbours(self,i,j,n):
        neighbours = []
        for add in self.next_loc_add:
            addi,addj = add
            ni = i + addi
            nj = j + addj
            if ni >= 0 and nj >= 0 and ni < n and nj < n:
                neighbours.append([ni,nj])
        return neighbours

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        # Solution Overview
        # simply make the knight moves and check that is it possible from moving current location to next location

        curr_move_number = 0
        row,col = 0,0
        if grid[row][col]!= curr_move_number:
            return False
        n = len(grid)
        while curr_move_number < n*n-1 :
            can_move_to_next_loc = False
            for neighbour in self.get_neighbours(row,col,n):
                n_row,n_col = neighbour
                if grid[n_row][n_col] == curr_move_number + 1:
                    row,col = n_row,n_col
                    can_move_to_next_loc = True
                    break
            if can_move_to_next_loc:
                curr_move_number += 1
            else:
                return False
        return True
