class Solution:
    def maxDepth(self, s: str) -> int:
        curr_depth ,max_depth = 0 , 0
        for c in s:
            if c == '(':
                curr_depth +=1 
            elif c == ')':
                curr_depth -= 1
            max_depth = max(max_depth,curr_depth)
        return max_depth
        
