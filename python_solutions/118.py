class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1 for j in range(i)] for i in range(1,numRows+1)]
        if numRows < 3:
            return res
        for row in range(3,numRows+1):
            for col in range(1,row-1):
                res[row-1][col] = res[row-2][col-1] + res[row-2][col]
        return res
