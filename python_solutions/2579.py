class Solution:
    def coloredCells(self, n: int) -> int:
        # solution overview
        # just think dude 
        if n == 1:
            return 1
        ans = 4 * (n-1)
        ans += 4 * (((n-2)*(n-2+1))//2)
        ans += 1
        return ans


