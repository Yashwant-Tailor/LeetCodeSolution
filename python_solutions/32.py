class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Solution Overview 
        # let's say at index i we encounter ')' , then it could be the right end of any valid substring starting from j < i
        # now till this index we would have some imbalance of opening parantheses '(' , so will need to keep track of index j < i , where we had same imbalance to update the lenght of new substring we have found
        # if we have imbalance of ')' then we can ignore the previous indices we have store for imbalance of '(' as this indicess will not contribute the left end of any substring starting in future
        imb_val = {}
        curr_imb = 0
        idx = 0
        max_len = 0
        imb_val[0] = -1
        while idx < len(s):
            if s[idx] == '(':
                curr_imb += 1
                imb_val[curr_imb] = idx
            elif curr_imb > 0:
                curr_imb -= 1
                max_len = max(max_len , idx - imb_val[curr_imb])
            else:
                curr_imb = 0
                imb_val.clear()
                imb_val[0] = idx
            idx += 1
        return max_len
        
