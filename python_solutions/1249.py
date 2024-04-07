class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_ind = []
        delete_idx = set()
        for idx,c in enumerate(s):
            if c == '(':
                open_ind.append(idx)
            elif c == ')':
                if len(open_ind) > 0:
                    open_ind.pop()
                else:
                    delete_idx.add(idx)
        while len(open_ind) > 0:
            delete_idx.add(open_ind.pop())
        new_str = ""
        for idx,c in enumerate(s):
            if idx not in delete_idx:
                new_str += c
        return new_str
        
