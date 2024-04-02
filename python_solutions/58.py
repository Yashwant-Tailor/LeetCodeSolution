class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = 0
        prev_word_len = 0
        while idx < len(s):
            while idx < len(s) and s[idx] == ' ':
                idx += 1
            if idx < len(s) and s[idx] != ' ':
                prev_word_len = 0
                while idx < len(s) and s[idx] != ' ':
                    prev_word_len += 1
                    idx += 1
        return prev_word_len
        
