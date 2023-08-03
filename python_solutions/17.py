class Solution:
    def update_res(self,curr_idx,letter_map,curr_str,digits,n,res):
        if curr_idx == n:
            if n > 0:
                res.append(curr_str)
            return
        for char in letter_map[digits[curr_idx]]:
            self.update_res(curr_idx + 1, letter_map,curr_str+char,digits,n,res)
    def letterCombinations(self, digits: str) -> List[str]:
        # Soution Overview
        # just simple maintain the all strings
        res = []
        letter_map = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        self.update_res(0,letter_map,'',digits,len(digits),res)
        return res
