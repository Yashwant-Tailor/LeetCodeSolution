class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for idx in range(len(s)):
            if s[idx] in s2t and t[idx] in t2s:
                if s2t[s[idx]] != t[idx] or t2s[t[idx]] != s[idx]:
                    return False
            elif s[idx] not in s2t and t[idx] not in t2s:
                s2t[s[idx]] = t[idx]
                t2s[t[idx]] = s[idx]
            else:
                return False
        return True
