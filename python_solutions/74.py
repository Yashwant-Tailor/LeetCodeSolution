class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Solution Overview
        # first perform the binary search based on the last integer of each row , i.e. we will discard the rows where we have last integer of that row smaller than the target because in this row all other integers are smaller than the last integer and our target is greater than the last integer 
        # after this binary serach the first row where our target is smaller or equal to the last element is row where we will either have the targe or don't , other rows we can discard safely 


        min_row = -1
        max_row = len(matrix)-1
        while min_row + 1 < max_row:
            mid_row = min_row + (max_row - min_row)//2
            if matrix[mid_row][-1] < target:
                min_row = mid_row
            else:
                max_row = mid_row
        if min_row == len(matrix):
            return False
        min_col = 0
        max_col = len(matrix[0])-1
        row = max_row
        while min_col <= max_col:
            mid_col = min_col + (max_col - min_col)//2
            if matrix[row][mid_col] == target:
                return True
            elif matrix[row][mid_col] > target:
                max_col = mid_col -1
            else:
                min_col = mid_col + 1
        return False
