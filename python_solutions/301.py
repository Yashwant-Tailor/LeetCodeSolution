class Solution:
    def get_min_op(self,s):
        op = 0
        idx = 0
        open_par = 0
        while idx < len(s):
            if s[idx] == '(':
                open_par += 1
            elif s[idx] == ')':
                if open_par > 0:
                    open_par -= 1
                else:
                    op += 1
            idx += 1
        op += open_par
        return op
    def get_valid_str(self,idx,s,res,min_op):
        if min_op == 0 and self.get_min_op(s) == 0:
            res.add(s)
            return
        if idx >= len(s):
            return
        if s[idx] == '(' or s[idx] == ')':
            self.get_valid_str(idx,s[:idx]+s[idx+1:],res,min_op-1)
        self.get_valid_str(idx+1,s,res,min_op)
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Solution Overview
        
        min_op = self.get_min_op(s)
        res = set()
        self.get_valid_str(0,s,res,min_op)
        return res
