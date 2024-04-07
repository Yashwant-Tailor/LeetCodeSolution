class Solution:
    def checkValidString(self, s: str) -> bool:
        star_stack = []
        open_stack = []
        for idx,c in enumerate(s):
            if c == '(':
                open_stack.append(idx)
            elif c == '*':
                star_stack.append(idx)
            else:
                if len(open_stack) > 0:
                    open_stack.pop()
                elif len(star_stack) > 0:
                    star_stack.pop()
                else:
                    return False
        while len(open_stack) > 0:
            if len(star_stack) == 0:
                return False
            elif star_stack.pop() < open_stack.pop():
                return False
        return True
            
            
        
