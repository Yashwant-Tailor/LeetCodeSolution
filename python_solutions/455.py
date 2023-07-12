class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gi = len(g)-1
        si = len(s) -1 
        ans = 0 
        while gi >= 0 and si >= 0:
            if g[gi] <= s[si]:
                ans += 1
                gi -= 1
                si -= 1
            else:
                gi -= 1
        return ans
