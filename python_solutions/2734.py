class Solution:
    def smallestString(self, s: str) -> str:
        # Solution Overview
        # if we focus on the 'a's in the string
        # then string will be in this form
        # ...a...a...a..a..a (where '...' substring could be empty)
        # then it will be first substring either appearing before 'a' or
        # in between two 'a's
        ans = ''
        idx = 0
        # as given in the question we need to perform this operations exactly one time
        is_op_applied = False
        while idx < len(s) and s[idx] == 'a':
            ans += s[idx]
            idx += 1
        while idx < len(s) and s[idx] != 'a':
            # mark that we have sucessfully applied the operation one time on the input string
            is_op_applied = True
            ans += chr(ord(s[idx])-1)
            idx += 1
        while idx < len(s):
            ans += s[idx]
            idx += 1
        if not is_op_applied:
            # make the last 'a' as 'z'
            ans = ans[:-1] + 'z'
        return ans
