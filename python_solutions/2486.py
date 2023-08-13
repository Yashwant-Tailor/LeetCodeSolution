class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # Solution Overview
        # simply match the character of s and t using pointer of s and t
        # after this matching if we have some non matching character in t then it will be the final answer
        s_idx = 0
        t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                t_idx += 1
            s_idx += 1
        return len(t)-t_idx
